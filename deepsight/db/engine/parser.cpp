// File for parsing a .ds weights file
#include "mylibrary.h"

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

