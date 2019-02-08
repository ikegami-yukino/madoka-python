// Copyright (c) 2012, Susumu Yata
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// 1. Redistributions of source code must retain the above copyright notice,
//    this list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright notice,
//    this list of conditions and the following disclaimer in the documentation
//    and/or other materials provided with the distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
// THE POSSIBILITY OF SUCH DAMAGE.

#ifndef MADOKA_CROQUIS_H
#define MADOKA_CROQUIS_H

#ifdef __cplusplus
 #include <cstring>
 #include <limits>
#endif  // __cplusplus

#include "file.h"
#include "hash.h"
#include "header.h"

#ifdef __cplusplus
namespace madoka {

const UInt64 CROQUIS_HASH_SIZE     = 3;

const UInt64 CROQUIS_ID_SIZE       = 128 / 3;
const UInt64 CROQUIS_MAX_ID        = (1ULL << CROQUIS_ID_SIZE) - 1;
const UInt64 CROQUIS_ID_MASK       = CROQUIS_MAX_ID;

const UInt64 CROQUIS_MIN_WIDTH     = 1;
const UInt64 CROQUIS_MAX_WIDTH     = CROQUIS_MAX_ID + 1;
const UInt64 CROQUIS_DEFAULT_WIDTH = 1ULL << 20;

const UInt64 CROQUIS_MIN_DEPTH     = 1;
const UInt64 CROQUIS_MAX_DEPTH     = 16;
const UInt64 CROQUIS_DEFAULT_DEPTH = CROQUIS_HASH_SIZE;

template <typename T>
class Croquis {
 public:
  Croquis() noexcept : file_(), header_(NULL), table_(NULL) {}
  ~Croquis() noexcept {}

  void create(UInt64 width = 0, UInt64 depth = 0, const char *path = NULL,
              int flags = 0, UInt64 seed = 0) throw(Exception) {
    Croquis new_croquis;
    new_croquis.create_(width, depth, path, flags, seed);
    new_croquis.swap(this);
  }
  void open(const char *path, int flags = 0) throw(Exception) {
    Croquis new_croquis;
    new_croquis.open_(path, flags);
    new_croquis.swap(this);
  }
  void close() noexcept {
    Croquis().swap(this);
  }

  void load(const char *path, int flags = 0) throw(Exception) {
    Croquis new_croquis;
    new_croquis.load_(path, flags);
    new_croquis.swap(this);
  }
  void save(const char *path, int flags = 0) const throw(Exception) {
    check_header();
    file_.save(path, flags);
  }

  UInt64 width() const noexcept {
    return header().width();
  }
  UInt64 width_mask() const noexcept {
    return header().width_mask();
  }
  UInt64 depth() const noexcept {
    return header().depth();
  }
  T max_value() const noexcept {
    return std::numeric_limits<T>::max();
  }
  UInt64 value_size() const noexcept {
    return header().value_size();
  }
  UInt64 seed() const noexcept {
    return header().seed();
  }
  UInt64 table_size() const noexcept {
    return header().table_size();
  }
  UInt64 file_size() const noexcept {
    return header().file_size();
  }
  int flags() const noexcept {
    return file_.flags();
  }

  T get(const void *key_addr, std::size_t key_size) const noexcept {
    T min_value = std::numeric_limits<T>::max();

    const T *table = table_;
    for (UInt64 i = 0; i < depth(); i += CROQUIS_HASH_SIZE) {
      UInt64 cell_ids[CROQUIS_HASH_SIZE];
      hash_(key_addr, key_size, seed() + i, cell_ids);

      const UInt64 end = ((depth() - i) >= CROQUIS_HASH_SIZE) ?
          CROQUIS_HASH_SIZE : (depth() - i);
      for (UInt64 j = 0; j < end; ++j) {
        const T value = table[cell_ids[j]];
        if (value <= static_cast<T>(0)) {
          return static_cast<T>(0);
        } else if (value < min_value) {
          min_value = value;
        }
        table += width();
      }
    }
    return min_value;
  }

  T get__(UInt64 table_id, UInt64 cell_id) const noexcept {
    return table_[(width() * table_id) + cell_id];
  }

  void set(const void *key_addr, std::size_t key_size, T value) noexcept {
    UInt64 cell_ids[CROQUIS_MAX_DEPTH + CROQUIS_HASH_SIZE - 1];
    hash(key_addr, key_size, cell_ids);

    T *table = table_;
    for (UInt64 i = 0; i < depth(); ++i) {
      T &cell = table[cell_ids[i]];
      if (cell < value) {
        cell = value;
      }
      table += width();
    }
  }

  void set__(UInt64 table_id, UInt64 cell_id, T value) const noexcept {
    T *table = table_;
    table[(width() * table_id) + cell_id] = value;
  }

  T add(const void *key_addr, std::size_t key_size, T value) noexcept {
    UInt64 cell_ids[CROQUIS_MAX_DEPTH + CROQUIS_HASH_SIZE - 1];
    hash(key_addr, key_size, cell_ids);

    T new_value = std::numeric_limits<T>::max();
    T *cells[CROQUIS_MAX_DEPTH];
    UInt64 num_cells = 0;

    T *table = table_;
    for (UInt64 i = 0; i < depth(); ++i) {
      T &cell = table[cell_ids[i]];
      if (cell < new_value) {
        cells[num_cells++] = &cell;
        if ((new_value - cell) > value) {
          new_value = cell + value;
        }
      }
      table += width();
    }

    for (UInt64 i = 0; i < num_cells; ++i) {
      if (*cells[i] < new_value) {
        *cells[i] = new_value;
      }
    }
    return new_value;
  }

  void clear() noexcept {
    std::memset(table_, 0, table_size());
  }

  void swap(Croquis *sketch) noexcept {
    file_.swap(&sketch->file_);
    util::swap(header_, sketch->header_);
    util::swap(table_, sketch->table_);
  }

  void copy(Croquis &src, const char *path = NULL,
            int flags = 0) throw(Exception) {
    create_(src.width(), src.depth(), path, flags, src.seed());
    std::memcpy(table_, src.table_, static_cast<std::size_t>(src.table_size()));
  }

  void shrink(Croquis &src, UInt64 width = 0,
              const char *path = NULL, int flags = 0) throw(Exception) {
    Croquis<T> new_sketch;
    new_sketch.shrink_(src, width, src.depth(), path, flags);
    new_sketch.swap(this);
  }

  void merge(const Croquis &rhs) throw(Exception){
    MADOKA_THROW_IF(width() != rhs.width());
    MADOKA_THROW_IF(depth() != rhs.depth());
    MADOKA_THROW_IF(seed() != rhs.seed());
      for (UInt64 table_id = 0; table_id < depth(); ++table_id) {
        for (UInt64 cell_id = 0; cell_id < width(); ++cell_id) {
        T lhs_value = get__(table_id, cell_id);
        T rhs_value = rhs.get__(table_id, cell_id);

        if ((lhs_value >= max_value()) ||
            (rhs_value >= (max_value() - lhs_value))) {
          lhs_value = max_value();
        } else {
          lhs_value += rhs_value;
        }
        set__(table_id, cell_id, lhs_value);
      }
    }
  }

  double inner_product(const Croquis &rhs, double *lhs_square_length = NULL,
                       double *rhs_square_length = NULL) const throw(Exception){
    MADOKA_THROW_IF(width() != rhs.width());
    MADOKA_THROW_IF(depth() != rhs.depth());
    MADOKA_THROW_IF(seed() != rhs.seed());

    double inner_product = std::numeric_limits<double>::max();
    for (UInt64 table_id = 0; table_id < depth(); ++table_id) {
      double current_inner_product = 0.0;
      double current_lhs_square_length = 0.0;
      double current_rhs_square_length = 0.0;
      for (UInt64 cell_id = 0; cell_id < width(); ++cell_id) {
        const double lhs_value =
            static_cast<double>(get__(table_id, cell_id));
        const double rhs_value =
            static_cast<double>(rhs.get__(table_id, cell_id));
        current_inner_product += lhs_value * rhs_value;
        if (lhs_square_length != NULL) {
          current_lhs_square_length += lhs_value * lhs_value;
        }
        if (rhs_square_length != NULL) {
          current_rhs_square_length += rhs_value * rhs_value;
        }
      }
      if (current_inner_product < inner_product) {
        inner_product = current_inner_product;
        if (lhs_square_length != NULL) {
          *lhs_square_length = current_lhs_square_length;
        }
        if (rhs_square_length != NULL) {
          *rhs_square_length = current_rhs_square_length;
        }
      }
    }
    return inner_product;
  }

 private:
  File file_;
  Header *header_;
  T *table_;

  const Header &header() const noexcept {
    return *header_;
  }
  Header &header() noexcept {
    return *header_;
  }

  void create_(UInt64 width, UInt64 depth, const char *path,
               int flags, UInt64 seed) throw(Exception) {
    if (width == 0) {
      width = CROQUIS_DEFAULT_WIDTH;
    }

    if (depth == 0) {
      depth = CROQUIS_DEFAULT_DEPTH;
    }

    MADOKA_THROW_IF(width < CROQUIS_MIN_WIDTH);
    MADOKA_THROW_IF(width > CROQUIS_MAX_WIDTH);
    MADOKA_THROW_IF(depth < CROQUIS_MIN_DEPTH);
    MADOKA_THROW_IF(depth > CROQUIS_MAX_DEPTH);

    const UInt64 table_size = sizeof(T) * width * depth;
    const UInt64 file_size = sizeof(Header) + table_size;
    MADOKA_THROW_IF(file_size > std::numeric_limits<std::size_t>::max());

    file_.create(path, static_cast<std::size_t>(file_size), flags);
    header_ = static_cast<Header *>(file_.addr());
    table_ = reinterpret_cast<T *>(header_ + 1);

    header().set_width(width);
    header().set_depth(depth);
    header().set_max_value(0);
    header().set_value_size(sizeof(T) * 8);
    header().set_seed(seed);
    header().set_table_size(table_size);
    header().set_file_size(file_size);
    check_header();

    clear();
  }

  void open_(const char *path, int flags) throw(Exception) {
    file_.open(path, flags);
    header_ = static_cast<Header *>(file_.addr());
    table_ = reinterpret_cast<T *>(header_ + 1);
    check_header();
  }

  void load_(const char *path, int flags) throw(Exception) {
    file_.load(path, flags);
    header_ = static_cast<Header *>(file_.addr());
    table_ = reinterpret_cast<T *>(header_ + 1);
    check_header();
  }

  void check_header() const throw(Exception) {
    MADOKA_THROW_IF(width() < CROQUIS_MIN_WIDTH);
    MADOKA_THROW_IF(width() > CROQUIS_MAX_WIDTH);
    MADOKA_THROW_IF((width_mask() != 0) && (width_mask() != (width() - 1)));
    MADOKA_THROW_IF(depth() < CROQUIS_MIN_DEPTH);
    MADOKA_THROW_IF(depth() > CROQUIS_MAX_DEPTH);
    MADOKA_THROW_IF(header().max_value() != 0);
    MADOKA_THROW_IF(value_size() != (sizeof(T) * 8));
    MADOKA_THROW_IF(table_size() != (sizeof(T) * width() * depth()));
    MADOKA_THROW_IF(file_size() != file_.size());
  }

  void hash(const void *key_addr, std::size_t key_size,
             UInt64 *cell_ids) const noexcept {
    for (UInt64 i = 0; i < depth(); i += CROQUIS_HASH_SIZE) {
      hash_(key_addr, key_size, seed() + i, cell_ids);
      cell_ids += CROQUIS_HASH_SIZE;
    }
  }

  void hash_(const void *key_addr, std::size_t key_size,
             UInt64 seed, UInt64 cell_ids[CROQUIS_HASH_SIZE]) const noexcept {
    UInt64 hash_values[2];
    Hash()(key_addr, key_size, seed, hash_values);

    cell_ids[0] = hash_values[0] & CROQUIS_ID_MASK;
    cell_ids[1] = ((hash_values[0] >> CROQUIS_ID_SIZE) |
        (hash_values[1] << (64 - CROQUIS_ID_SIZE))) & CROQUIS_ID_MASK;
    cell_ids[2] = hash_values[1] >> (64 - CROQUIS_ID_SIZE);

    if (width_mask() != 0) {
      cell_ids[0] &= width_mask();
      cell_ids[1] &= width_mask();
      cell_ids[2] &= width_mask();
    } else {
      cell_ids[0] %= width();
      cell_ids[1] %= width();
      cell_ids[2] %= width();
    }
  }

  void shrink_(const Croquis &src, UInt64 width, UInt64 depth,
               const char *path, int flags) throw(Exception) {
    if (width == 0) {
      width = src.width();
    }

    MADOKA_THROW_IF(src.width() == 0);
    MADOKA_THROW_IF(width > src.width());
    MADOKA_THROW_IF((src.width() % width) != 0);

    create_(width, depth, path, flags, src.seed());

    width = this->width();

    for (UInt64 table_id = 0; table_id < src.depth(); ++table_id) {
      for (UInt64 cell_id = 0; cell_id < width; ++cell_id) {
        T value = src.get__(table_id, cell_id);
        set__(table_id, cell_id, value);
      }

      for (UInt64 offset = width; offset < src.width(); offset += width) {
        for (UInt64 cell_id = 0; cell_id < width; ++cell_id) {
          T value = src.get__(table_id, offset + cell_id);
          if (value > get__(table_id, cell_id)) {
            set__(table_id, cell_id, value);
          }
        }
      }
    }
  }

  // Disallows copy and assignment.
  Croquis(const Croquis &);
  Croquis &operator=(const Croquis &);
};

}  // namespace madoka
#endif  // __cplusplus

#endif  // MADOKA_CROQUIS_H
