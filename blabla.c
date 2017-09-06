#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <stdbool.h>

struct point {
    int x;
    int y;
};

float slope(int x1, int y1, int x2, int y2);


int main() {
    struct point pos[100];
    double a;
    double b;
    int i,j,k;
    
    srand(time(NULL));
    
    for(i = 0; i < 100; i++){
        pos[i].x = rand()%1000;
        pos[i].y = rand()%1000;
    }
    
    int count1 = 0, count = 0;
    int best = 0;
    
    for(i = 0; i < 100; i++){
        for(j =  i + 1; j < 100; j++){
        	if (pos[i].x == pos[j].x){
        	    count++;
        	    continue;
        	} else {
			a = (pos[j].y - pos[i].y)/(pos[j].x - pos[i].x);
			b = pos[i].y - a*pos[i].x;
        	
        	    for(k = 0; k < 100; k++){
				    if (pos[j].y == (a*pos[j].x + b)){
					    count++;
				    }
			    }
		    if (count > best) best = count;
		    count = 0;
        	}
        }
    }
	
    printf("max # of points are collinear is %d", count);
    return 0;
}
