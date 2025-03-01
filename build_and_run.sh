#!/bin/bash

# Directory names
BUILD_DIR="build"

# Function to clean the project
clean_project() {
    echo "Cleaning the project..."
    if [ -d "$BUILD_DIR" ]; then
        rm -rf "$BUILD_DIR" || { echo "Failed to clean the project"; exit 1; }
        echo "Build directory removed."
    else
        echo "No build directory found. Skipping clean step."
    fi
}

# Function to configure, build, and run the project
build_and_run_project() {
    echo "Configuring the project..."
    cmake -S . -B "$BUILD_DIR" || { echo "CMake configuration failed"; exit 1; }

    echo "Building and running the project..."
    cmake --build "$BUILD_DIR" --target build_and_run || { echo "Build and run failed"; exit 1; }
}

# Main script logic
if [ "$1" == "clean" ]; then
    # Clean the project and then build/run
    clean_project
    build_and_run_project
else
    # Build and run without cleaning
    build_and_run_project
fi

echo "Script execution completed!"
