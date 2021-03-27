#include<iostream>

int main()
{
	using namespace std;

	int total = 0;
	for (int i = 1; i <= 100; i += 2)
	{
		total = total + i;
	}
	cout << "1부터 100까지의 홀수의 합은 " << total << "입니다." << endl;
	return 0;
}