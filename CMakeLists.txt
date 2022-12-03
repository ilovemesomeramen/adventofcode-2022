cmake_minimum_required(VERSION 3.24)
project(adventofcode_2022)

set(CMAKE_CXX_STANDARD 23)

FILE(GLOB DAYS RELATIVE ${CMAKE_SOURCE_DIR} ${CMAKE_SOURCE_DIR}/day*)

set(CMAKE_CXX_FLAGS "-Wall -Wextra")
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

foreach(day ${DAYS})
    set(CPP_DAY_DIR ${CMAKE_SOURCE_DIR}/${day}/c++)
    set(CPP_DAY_SOURCE_DIR ${CPP_DAY_DIR}/src)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CPP_DAY_DIR})
    FILE(GLOB PARTS RELATIVE ${CPP_DAY_SOURCE_DIR} ${CPP_DAY_SOURCE_DIR}/part*.cpp)
    foreach(part ${PARTS})
        get_filename_component(c_part ${part} NAME_WLE)
        add_executable(${day}-${c_part} ${CPP_DAY_SOURCE_DIR}/${part})
    endforeach()
endforeach()


