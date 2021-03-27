#include <iostream>
int main()
{
	using namespace std;

	cout << "값 5개의 합계와 평균을 구합니다." << endl;
	cout << "값 5개를 입력하십히오." << endl;

	double number;
	double sum = 0.0;

	for (int i = 1; i <= 5; i++) {
		cout << "값" << i << ":";
		cin >> number;
		sum += number;   //sum=sum+number

		cout << "checking sum"<< sum << endl;   //sum확인
	}

	cout << "값 5개가 모두 입력되었습니다." << endl;
	cout << "입력한 값 5개의 합계는 " << sum << "입니다." << endl;
	cout << "입력한 값 5개의 평균은 " << sum / 5 << "입니다." << endl;
	cout << "감사합니다." << endl;

	return 0;
}