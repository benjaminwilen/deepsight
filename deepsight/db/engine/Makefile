# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -fPIC -Wall -Wextra -std=c++11

# Directories
SRCDIR = .
BUILDDIR = build
LIBDIR = lib

# Files
TARGET = main
LIBNAME = compress
LIBFILE = $(LIBDIR)/lib$(LIBNAME).so
SOURCES = $(SRCDIR)/main.cpp $(SRCDIR)/compress.cpp
HEADERS = $(SRCDIR)/compress.h

# Build rules
all: $(TARGET)

$(TARGET): $(BUILDDIR)/main.o $(LIBFILE)
	$(CXX) $(BUILDDIR)/main.o -L$(LIBDIR) -l$(LIBNAME) -o $(TARGET)

$(BUILDDIR)/main.o: $(SRCDIR)/main.cpp $(HEADERS)
	@mkdir -p $(BUILDDIR)
	$(CXX) $(CXXFLAGS) -I$(SRCDIR) -c $(SRCDIR)/main.cpp -o $(BUILDDIR)/main.o

$(LIBFILE): $(BUILDDIR)/compress.o
	@mkdir -p $(LIBDIR)
	$(CXX) -shared -o $(LIBFILE) $(BUILDDIR)/compress.o

$(BUILDDIR)/compress.o: $(SRCDIR)/compress.cpp $(HEADERS)
	@mkdir -p $(BUILDDIR)
	$(CXX) $(CXXFLAGS) -I$(SRCDIR) -c $(SRCDIR)/compress.cpp -o $(BUILDDIR)/compress.o

clean:
	rm -rf $(BUILDDIR) $(LIBDIR) $(TARGET)

.PHONY: all clean
