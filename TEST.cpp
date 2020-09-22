#include<iostream>
using namespace std;
int main(){
	while(true){
		int n;
		cin >> n;
		if(n==42)
			return 0;
		else
			cout << n << endl;
	}
	return 0;
}