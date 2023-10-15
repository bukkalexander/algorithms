set(TARGET ${MERGE_SORT_MODULE_NAME})

add_executable(${TARGET} main.cpp)

target_link_libraries(${TARGET} PRIVATE
    ${LIB_UTILS}
)