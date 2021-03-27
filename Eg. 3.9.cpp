#include <iostream>

int main()
{
	using namespace std;
	int val = 85;
	char level;

	switch (val / 10) {
	    case 9:level = 'A'; break;
		case 8:level = 'B'; break;
		case 7:level = 'C'; break;
		default:level = 'D'; break;

	}
	cout << "Hazard value " << val << " corresponds to level" << level << endl;

	return 0;
}