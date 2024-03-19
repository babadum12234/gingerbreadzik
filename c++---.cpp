#include<iostream>
#include<string>
#include<time.h>
using namespace std;
 
int main() {
	srand(time(NULL));
	cout << "bomba jest niegrzeczny" << endl;
	//	int a;
	//	cin >> a;
	//	int b;
	//	cin >> b;
	//	int c;
	//	cin >> c;
		//string tekst;
		//getline(cin, tekst);
		//cout << tekst<<  endl;
		//cout << pow(a, b) << endl;		//potęgowanie
		//cout << sqrt(c) << endl;		//pierwiastek
		//// && = and   || = or 6
 
		//const float CSTLA = 234.57543456;		//stała
 
		//if (a > 6) {
		//	cout << "ty k****";
		//}
		//else if (a > 25) {
		//	cout << "sruu";
		//}
		//else {
		//	cout << "asda";
		//}
 
	//short liczba;
	//cin >> liczba;
	//bool ujemna = (liczba < 0) ? true : false;
	//while(liczba=liczba){
	//	switch (liczba) {
	//	case 1: cout << "ciemny";			//wykona się to i ten niżej
	//	case 2:cout << "czarny"; 	//wykona się tylko ten
	//	case 3:cout << "n";
	//	case 4:cout << "i";
	//	case 5:cout << "g";
	//	case 6:cout << "e";
	//	case 7:cout << "r";
	//	default: cout << "NIGER"; liczba = 3;
	//	}
	//}
 
 
	/*	short g;
		cin >> g;
		long cos = 1;
		for (int i = 1; i < g+1; i++)
			cos = i * cos;
		cout << cos;*/
	/*int fg;
	cin >> fg;
	long long a = 0;
	long long b = 1;
	short i=0;
	while (i<fg) {
		i++;
		a = a + b;
		b = a + b;
		cout << a<<" ";
		cout << b<<" ";
	}*/
	//int i = 10;
	//do {	//wykonuje się choć raz
	//	cout << rand()%10+1 << endl;
	//	//<a;b>
	//	//rand()%(b-a+1)+a
	//} while (i <= 100);
 
 
	//rand();	//od 0 do 32000 ok + zawsze ta sama kolejność
	/*short l = rand()%100+1;
	short s;
	short life = 10;
	for (int i = 20; i>0; i--) {
		cin >> s;
		if (life == 0) {
			cout << "niestety przegrales :(" << endl;
			break;
		}
		if (s == l) {
			cout << "brawo zgadles :)!" << endl;
			break;
		}
		else if (s > l) {
			cout << "za duza liczba";
			life--;
		}
		else {
			cout << "za mala liczba";
			life--;
		}
	}*/
 
	//tablice danych :
	//a) statyczne		TypDanych nazwa[<ilosc>]
	//  int liczby[10] = { 1,4,9 };
	//  int dlugosc = sizeof(liczby) / sizeof(int);		//len liczby
	//b) dynamiczne
	//c) kontenery STL np vector
 
	//short setka = rand() % 10 + 1;
// 	short n, cont, l=0;	
// 	n = 10;
	int tab[10] = { 4,3,7,1,3,2,5,8,0,5 };\
// 	bombatymojbobelku(n, tab[], cont);
// 	return 0;
// }
 
// void bombatymojbobelku(short n, int tab[], short cont, short l) {
// 	for (int i = 0; i < n; i++)
// 		if (tab[i] < tab[i = +1])
// 			cont = tab[i];
// 			tab[i] = tab[i + 1];
// 			tab[i + 1] = cont;
// 			l++
// 	cout << tab;
    cout << sizeof(tab);
 
}