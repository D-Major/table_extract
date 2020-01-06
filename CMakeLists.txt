cmake_minimum_required(VERSION 3.13)
project(table_extract)

set(CMAKE_CXX_STANDARD 11)

set(CUDA_INCLUDE_DIRS /usr/local/cuda)
set(OpenCV_DIR /usr/local/bin/opencv-3.4.5-cpu/share/OpenCV)
find_package(OpenCV REQUIRED)
set(OpenCV_LIB_DIR ${OpenCV_INSTALL_PATH}/lib)
message(STATUS "OpenCV版本: ${OpenCV_VERSION}")
message(STATUS "    头文件目录：${OpenCV_INCLUDE_DIRS}")
message(STATUS "    库文件目录：${OpenCV_LIB_DIR}")
message(STATUS "    库文件列表：${OpenCV_LIBS}")
include_directories(/usr/local/bin/opencv-3.4.5-cpu/include/opencv2 ${OpenCV_INCLUDE_DIRS})
link_directories(${OpenCV_LIB_DIR} /usr/local/bin/opencv-3.4.5-cpu/lib)

add_executable(table_extract main.cpp)