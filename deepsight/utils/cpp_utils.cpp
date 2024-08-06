// File for parsing a .ds weights file
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

class FileStreamWrapper {
public:
    FileStreamWrapper() = default;

    // Open file for reading and writing
    bool open(const std::string& filename, std::ios::openmode mode) {
        file.open(filename, mode);
        if (file.is_open()) {
            this->filename = filename;
            return true;
        }
        return false;
    }

    // Close the file
    void close() {
        file.close();
    }

    // Check if file is open
    bool is_open() const {
        return file.is_open();
    }

    // Get the filename
    std::string get_filename() const {
        return filename;
    }

    // Access the underlying fstream object
    std::fstream& get_stream() {
        return file;
    }

private:
    std::fstream file;
    std::string filename;
};
