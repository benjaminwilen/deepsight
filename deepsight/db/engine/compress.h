#ifndef COMPRESS_H
#define COMPRESS_H

#if defined(_WIN32) || defined(_WIN64)
  #define EXPORT __declspec(dllexport)
#else
  #define EXPORT
#endif

// Function declaration
extern "C" {
    EXPORT void _compress_weights();
}

#endif // COMPRESS_H