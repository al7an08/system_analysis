#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

// Индексация номера строки и столбца идёт с 0

int main(int argc, char *argv[])
{
    // Проверка количества аргументов
    if (argc != 4)
    {
        std::cerr << "Usage: " << argv[0] << " <csv_file> <row_number> <col_number>" << std::endl;
        return 1;
    }

    // Чтение аргументов
    std::string filePath = argv[1];
    int row = std::stoi(argv[2]);
    int col = std::stoi(argv[3]);

    // Открытие файла
    std::ifstream file(filePath);
    if (!file.is_open())
    {
        std::cerr << "Error: Unable to open file " << filePath << std::endl;
        return 1;
    }

    std::string line;
    int currentRow = 0;

    // Проход по строкам файла
    while (std::getline(file, line))
    {
        if (currentRow == row)
        {
            std::stringstream lineStream(line);
            std::string cell;
            int currentCol = 0;

            // Проход по столбцам строки
            while (std::getline(lineStream, cell, ','))
            {
                if (currentCol == col)
                {
                    std::cout << "Value at row " << row << ", column " << col << " is: " << cell << std::endl;
                    return 0;
                }
                currentCol++;
            }
            std::cerr << "Error: Column number " << col << " is out of bounds." << std::endl;
            return 1;
        }
        currentRow++;
    }

    std::cerr << "Error: Row number " << row << " is out of bounds." << std::endl;
    return 1;
}