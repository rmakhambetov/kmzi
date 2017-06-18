#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void r_array(int g, bool *r);
void r_shake(int g, bool *r, int q);
void r_print(int g, bool *r);

int main()
{
	unsigned size = 0;
	char buffer;
	char key[] = "Der67JJk";
	bool r1[19];
	bool r2[22];
	bool r3[23];
	bool rr[64];
	bool F;
	//int i, j, k;
	FILE *inpFile = fopen("..\\Debug\\Der67JJk.jpg", "rb");
	FILE *outFile = fopen("..\\Debug\\2.jpg", "wb");
	fseek(inpFile, 0, SEEK_END);
	size = ftell(inpFile);
	fseek(inpFile, 0, SEEK_SET);

	for (int i = 0; i < 8; i++)
	{
		for (int j = 7; j >= 0; j--)
		{
			rr[i*8+j] = key[i] & 1;
			key[i] >>= 1;
					
		}
	}

	/*for (int k = 0; k < 64; k++)
	{
		if (rr[k] == false)  printf("0");
		else printf("1");
	}*/

	//for (int i = 0; i < 19; i++)
	//{
	//	r1[i] = 0;
	//}
	//for (int i = 0; i < 22; i++)
	//{
	//	r2[i] = 0;
	//}
	//for (int i = 0; i < 23; i++)
	//{
	//	r3[i] = 0;
	//}
	r_array(19, r1);
	r_array(22, r2);
	r_array(23, r3);
	for (int i = 0; i < 64; i++)
	{
		r1[0] ^= rr[i];
		r2[0] ^= rr[i];
		r3[0] ^= rr[i];
		r_shake(19, r1, 1);
		r_shake(22, r2, 2);
		r_shake(23, r3, 3);
	}



	for (int i = 0; i < 100; i++)
	{
		F = r1[8] & r2[10] | r1[8] & r3[10] | r2[10] & r3[10];
		if (F == r1[8]) {r_shake(19, r1, 1);}
		if (F == r2[10]) {r_shake(22, r2, 2);}
		if (F == r3[10]) {r_shake(23, r3, 3);}
	}

	r_print(19, r1);
	r_print(22, r2);
	r_print(23, r3);

	for (unsigned i = 0; i < size; i++)
	{
		fscanf(inpFile,"%c",&buffer);
		char G = 0;
		for (int k = 0; k < 8; k++){
			G <<= 1;
			F = r1[8] & r2[10] | r1[8] & r3[10] | r2[10] & r3[10];
			if (F == r1[8]){
				G ^= r1[18]; r_shake(19, r1, 1);
			}
			if (F == r2[10]){
				G ^= r2[21]; r_shake(22, r2, 2);
			}
			if (F == r3[10]){
				G ^= r3[22]; r_shake(23, r3, 3);
			}
		
		}

		fprintf(outFile,"%c",buffer^G);

	}



	/*for (int k = 0; k < 19; k++)
	{
		if (r1[k] == false)  printf("0");
		else printf("1");
	}*/
	
	/*for (unsigned i = 0; i < size; i++)
	{
		fscanf(inpFile,"%c",&buffer);
		fprintf(outFile,"%c",buffer);

	}*/

	
	printf("\nsize = %i\n", size);

	system("pause");
	return 0;
}

void r_array(int g, bool *r)
{
	for (int i = 0; i < g; i++)
	{
		r[i] = 0;
	}
}

void r_shake(int g, bool *r,int q)
{
	bool tmp;
	switch (q)
	{
	case 1: tmp = r[18] ^ r[17] ^ r[16] ^ r[13];
		break;
	case 2: tmp = r[21] ^ r[20];
		break;
	case 3: tmp = r[22] ^ r[21] ^ r[20] ^ r[7];
		break;
	}
	
	

	for (int i = g - 1; i > 0; i--)
	{
		r[i] = r[i - 1];
	}
	r[0] = tmp;
}

void r_print(int g, bool *r)
{
	for (int k = 0; k < g; k++)
	{
		if (r[k] == false)  printf("0");
		else printf("1");
	}
	printf("\n");
}