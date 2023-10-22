add_executable(my_tests test_merge_sort.cpp)

target_include_directories(my_tests PRIVATE
    ${CMAKE_SOURCE_DIR}/external/googletest/include
)

target_link_libraries(my_tests PRIVATE
    ${CMAKE_SOURCE_DIR}/external/googletest/lib/libgtest.a
    ${CMAKE_SOURCE_DIR}/external/googletest/lib/libgtest_main.a
)

add_test(NAME MY_TESTS COMMAND my_tests)