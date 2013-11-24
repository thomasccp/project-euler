#include "problem1.hpp"

using namespace std;

Problem1::Problem1(){
	_limit = 999;
}

Problem1::Problem1(int limit){
	_limit = limit;
}

int Problem1::getSumofMultiple(int num){
	int bound = _limit/num;
	return num*(1+bound)*bound/2;
}
