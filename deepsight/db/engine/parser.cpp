// File for parsing a .ds weights file
#include "cpp_utils.h"

#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

std::string parse_header(const std::fstream& filePath) {
    """
    Parse header file given a fstream
    """
    std::string firstLine;
    if (std::getline(inputFile, firstLine)) {
        // Split the line by '$' signs
        
    } else {
        std::cerr << "The file is empty or an error occurred while reading the first line." << std::endl;
    }     
    
} 

cpp_utils::FileStreamWrapper read_weights_file(const std::string& filePath) {
    cpp_utils::FileStreamWrapper inputFile("example.txt");

    if (inputFile.is_open()) {
        return inputFile;
    } else {
        throw std::runtime_error("Failed to open the file.");
    } 
} 