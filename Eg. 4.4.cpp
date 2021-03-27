#include <iostream>

int main()
{
	using namespace std;
	const int FST = 4;
	const int SND = 3;
	int f, s;
	int sum = 0;
	int score[FST][SND] = {
		{65,70,55},
		{75,85,79},
		{98,92,88},
		{80,82,89} };


	//각 학생별 총점과 평균구하기
	for (f = 0; f < FST; f++) {
		sum = 0;
		for (s = 0; s < SND; s++) {
			sum += score[f][s];
		}
		cout << f + 1 << "번째 학생 total= " << sum << ", average= " << (double)sum / FST << endl;
	}


	/*for (s = 0; s < SND; s++) {
		sum = 0;
		for (f = 0; f < FST; f++) {
			sum += score[f][s];
		}
		cout << s + 1 << " total = " << sum << ", average = " << (double)sum / FST << endl;
	}*/

	return 0;
}