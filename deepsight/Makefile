# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Wall -Wextra -std=c++17 -fPIC

# Targets
TARGET = test/db/engine/test_compress
LIBRARY = db/engine/parser.so

# Source files
LIBRARY_SRC = test/db/engine/test_compress
MAIN_SRC = db/engine/parser.cpp

# Object files
LIBRARY_OBJ = $(LIBRARY_SRC:.cpp=.o)
MAIN_OBJ = $(MAIN_SRC:.cpp=.o)

# Include paths
INCLUDES = -Ilib

# Default target
all: $(TARGET)

# Build the shared library
$(LIBRARY): $(LIBRARY_OBJ)
	$(CXX) -shared -o $@ $^

# Build the main program
$(TARGET): $(MAIN_OBJ) $(LIBRARY)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -o $@ $^ -Llib -lmylibrary

# Compile library object file
lib/%.o: lib/%.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

# Compile main object file
src/%.o: src/%.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

# Clean up build files
clean:
	rm -f $(TARGET) $(LIBRARY) $(LIBRARY_OBJ) $(MAIN_OBJ)

# Rebuild everything
rebuild: clean all