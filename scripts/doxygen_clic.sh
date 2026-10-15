#!/usr/bin/env bash
# Generate the CLIc Doxygen XML read by breathe (conf.py: breathe_projects["CLIc"]).
#
# CLIc's Doxyfile is used as-is, with the backend macros predefined so that the classes
# guarded by `#if USE_OPENCL` / `#if USE_CUDA` / `#if USE_METAL` (e.g. OpenCLBackend,
# CUDABackend) are documented.
#
# Requires doxygen < 1.11: newer versions write "=0", "=default" and "=delete" into the
# member type, which breathe fails to parse.
set -euo pipefail

cd _submodules/clic/docs
mkdir -p build/doxygen  # OUTPUT_DIRECTORY, doxygen does not create parent directories
{
    cat Doxyfile
    echo "PREDEFINED = USE_OPENCL=1 USE_CUDA=1 USE_METAL=1"
} | doxygen -
