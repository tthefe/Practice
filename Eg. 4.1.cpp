#include <iostream>

int main()
{
	using namespace std;

	/*변수의 값을 선언하는 법
	int sts = 0;
	int s(0);
	int s{ 0 };*/

	int s, sum = 0;
	int score[8] = { 75,85,100,60,55,88,45,95 };

	for (s = 0; s < 8; s++) {
		sum += score[s];
	}

	/*최근 C++에서 지원하는 새로운 형식
	for (int i : score) {
		sum += i;
	}*/

	cout << "Total: " << sum << endl;
	cout << "Average: " << (double)sum / 8 << endl;   //sum을 double형으로 강제로 형변환
	
	return 0;
}