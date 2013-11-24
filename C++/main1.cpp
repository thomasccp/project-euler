#include <iostream>
#include "problem1.hpp"
using namespace std;

int main(){
	Problem1 p = Problem1(999);
	int sum = p.getSumofMultiple(3)+p.getSumofMultiple(5)-p.getSumofMultiple(15);
	cout << sum << endl;
	return 0;
}
