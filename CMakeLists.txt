cmake_minimum_required(VERSION 3.22.1)

project(algorithms VERSION 1.0)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_INCLUDE_PATH ${CMAKE_SOURCE_DIR}/cmake)
include(${CMAKE_INCLUDE_PATH}/path.cmake)

add_subdirectory(${INSERTION_SORT_DIR_PATH})
add_subdirectory(${MERGE_SORT_DIR_PATH})
add_subdirectory(${UTILS_DIR_PATH})

enable_testing()
add_subdirectory(${MERGE_SORT_DIR_PATH}/test)