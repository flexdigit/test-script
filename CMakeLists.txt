cmake_minimum_required(VERSION 3.10)
project(PythonScriptExample)

# Ensure Python is found
find_package(Python3 REQUIRED)

# Add a custom target to run the Python script
add_custom_target(
    run_script
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/print_file.py ${CMAKE_SOURCE_DIR}/file_to_print.txt
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Running Python script to print file contents"
)

# Add a custom target to build and run the project
add_custom_target(
    build_and_run
    DEPENDS run_script
    COMMENT "Building and running the project"
)
