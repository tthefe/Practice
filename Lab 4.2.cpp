#include<iostream>

int main()
{
	using namespace std;
	int s;
	int f;
	int total = 0;
	int score1[3][3] = {0};
	int score2[3][3] = { 0 };
	int A[3][3] = {
		{1,1,1},
		{2,2,2},
		{3,3,3}
	};
	int B[3][3] = {
		{1,2,3},
		{1,2,3},
		{1,2,3}
	};

	//3*3행렬 합
	for (s = 0; s < 3; s++) {
		for (f = 0; f < 3; f++) {
			score1[s][f]=A[s][f] + B[s][f];
		}
	}
	//3*3행렬 출력
	for (s = 0; s < 3; s++) {
		for (f = 0; f < 3; f++) {
			cout << score1[s][f];
			if (f < 2) {
				cout << " ";
			}
		}
		cout << endl;
	}






	for (s = 0; s < 3; s++) {
		for (f = 0; f < 3; f++) {
			total + = A[s][f] * B[f][s];
			.
		}
	}

	return 0;
}