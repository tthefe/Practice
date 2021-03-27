#include <iostream>

int main()
{
	using namespace std;
	const int ArSize = 20;   //const==변수를 상수로 선언할 때 사용, 프로그램 중간에 ArSize에 다른 값이 대입되면 에러 발생
                             //#define Arsize 20과 동일한 의미=컴파일 전에 전처리기에 의해서 숫자로 치환
	char name[ArSize];
	char dessert[ArSize];

	cout << "Enter your name: " << endl;;
	cin >> name;
	cout << "Enter your favorite dessert: " << endl;
	cin >> dessert;
	cout << "I will serve delicious " << dessert;
	cout << " for you, " << name << "!" << endl;

	return 0;
}