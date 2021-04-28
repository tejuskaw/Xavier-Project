#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <iostream>

using namespace std ;


pthread_t *philosophers;
pthread_mutex_t *forks;

int philosophers_count;


void eating(int a){

	cout << "Philosopher "<<a+1 << " is eating the food "<< endl;

	sleep(1 + rand()%10);
}

void* philosopher(void* args){
	int a = 0,one,two;
	while(!pthread_equal(*(philosophers+a),pthread_self()) && a < philosophers_count){
		a++;
	}

	while(1){

		cout << "Philosopher " << a+1 << " is thinking "<< endl;

		sleep(1 + rand()%10);
		
		one = a;
		two = (a+1)%philosophers_count;

		pthread_mutex_lock(forks + (one>two?two:one));
		pthread_mutex_lock(forks + (one<two?two:one));
		eating(a);
		pthread_mutex_unlock(forks+one);
		pthread_mutex_unlock(forks+two);
	}

	return NULL;
}


int main(void){
	int a,errr;

	srand(time(NULL));

	cout << "Enter number of philosophers you need:"<< endl;
	cin >> philosophers_count ;
	philosophers = (pthread_t*) malloc(philosophers_count*sizeof(pthread_t));
	forks = (pthread_mutex_t*) malloc(philosophers_count*sizeof(pthread_mutex_t));

	for(a=0;a<philosophers_count;++a)
		if(pthread_mutex_init(forks+a,NULL) != 0){
			cout << "Failed initializing the fork "<< a+1 << endl;
			return 1;
		}

	for(a=0;a<philosophers_count;++a){
		errr = pthread_create(philosophers+a,NULL,&philosopher,NULL);

		if(errr != 0){
			cout << "Error creating the philosopher: " << strerror(errr) << endl;
		}else{
			cout << "Successfully created the philosopher " << a+1 << endl;
		}
	}

	for(a=0;a<philosophers_count;++a)
		pthread_join(*(philosophers+a),NULL);

	free(philosophers);
	free(forks);

	return 0;
}