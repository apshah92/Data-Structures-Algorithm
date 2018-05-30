Exercise R 2.7:

Implementations of Vector Based Binary Tree in C++.
Methods: root, parent, leftChild, rightChild, isInternal, isExternal and 
isRoot

C++ program:

#include <vector>
using namespace std;



template <typename T>
class BinaryTree {

public:
    class Position {
    private:
        int key;
    public:
        Position(int k) : key(k) {}
        friend class BinaryTree;
    };


protected:

    vector<T> *array;

public:
    BinaryTree() {
        array = new vector<T>;
        array->push_back(T());
    }

    int size() {
        return int(array->size()) - 1;
    }

    ~BinaryTree() {
        delete [] array;
    }

Position root() {
        return Position(array[1]);
    }

    bool isRoot(const Position& p) {
        return p.key ==1;
    }

    bool isLeft(const Position& p) {
        return p.key % 2 == 0;
    }



    Position parent(const Position& p) {
        return Position(array->at(p.key / 2));

    }

    Position leftChild(const Position& p) {
        return Position(array->at(p.key * 2));
    }
    Position rightChild(const Position& p) {
        return Position(array->at(p.key * 2 + 1));
    }
bool isExternal(const Position& p) {
        return p.key * 2 > size();
    }
 bool isInternal(const Position& p) {
        return !isExternal(p);
    }
};
