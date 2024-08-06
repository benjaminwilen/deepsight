// File for evaluation of a WeightsFile object
#include "mylibrary.h"

#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

std::string _compress_weights(const std::string& filePath) {
    """
    Compression for weights file

    ** Currently just returns file contents with no compression
    """
    // TODO: implement compression
    
    if (!file) {
        throw std::runtime_error("Unable to open file: " + filePath);
    }

    std::stringstream buffer;
    buffer << file.rdbuf();
    if (buffer.fail()) {
        throw std::runtime_error("Error reading file: " + filePath);
    }
    
    return buffer.str();
} 
