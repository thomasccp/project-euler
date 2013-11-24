#include "problem2.hpp"

using namespace std;

Problem2::Problem2(){
	_limit = 4000000;
}

Problem2::Problem2(int limit){
	_limit = limit;
}

int Problem2::calculate(){
	int first = 2;
	int second = 8;
	int sum = first;
	int temp;
	while (second<_limit){
		sum += second;
		temp = second;
		second = 4*second+first;
		first = temp;
	}
	return sum;
}
