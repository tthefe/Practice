#include <iostream>

int main()
{
	using namespace std;

	int a = 1;
	int b = 2;
	float f1 = a / b;
	float f2 = float(a / b);
	float f3 = (float)a / b;
	float f4 = float(a) / b;
	float f5 = a / float(b);

	cout << f1 << endl;
	cout << f2 << endl;
	cout << f3 << endl;
	cout << f4 << endl;
	cout << f5 << endl;

	cout << "\n\n" << "-----------------" << "\n\n";

	double zero = 0.0;
	double posinf = 5.0 / zero;
	double neginf = -5.0 / zero;
	double nan= zero / zero;

	//Inf=Infinite Number
	//Ind=Indeeterminate Number
	//Nan=Not a number

	cout <<posinf<< ' '<<isinf(posinf) << endl; //1(1은 맞고 0은 틀린 것)
	cout <<neginf<< ' '<<isinf(neginf)<< endl;
	cout <<nan<< ' '<<isnan(nan) << endl;

	cout << 2.3 << " " << isnan(2.3) << endl;


	return 0;
}