#include <iostream>

int main()
{
	using namespace std;

	/*������ ���� �����ϴ� ��
	int sts = 0;
	int s(0);
	int s{ 0 };*/

	int s, sum = 0;
	int score[8] = { 75,85,100,60,55,88,45,95 };

	for (s = 0; s < 8; s++) {
		sum += score[s];
	}

	/*�ֱ� C++���� �����ϴ� ���ο� ����
	for (int i : score) {
		sum += i;
	}*/

	cout << "Total: " << sum << endl;
	cout << "Average: " << (double)sum / 8 << endl;   //sum�� double������ ������ ����ȯ
	
	return 0;
}