#include<iostream>

int main()
{
	using namespace std;
	bool tf;

	tf = true && true;
	cout << "true && true= " << tf << endl;
	
	tf = true && false;
	cout << 'true&&false ' << tf << endl;

	tf = false || false;
	cout << 'false||false= ' << tf << endl;

	tf = true || false;
	cout << 'true||false= ' << tf << endl;

	tf = !true;
	cout << "!true= " << tf << endl;

	return 0;
}