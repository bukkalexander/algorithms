set(TARGET utils)

add_library(${TARGET} SHARED
    src/utils.cpp
)

target_include_directories(${TARGET} PUBLIC include)