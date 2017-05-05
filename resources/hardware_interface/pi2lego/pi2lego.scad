/* pi 2 lego connector */

/*
The Raspberrry Pi 3 has 4 holes in a 58mm X 49mm.

*/

MOUNT_WIDTH = 58.0;
MOUNT_HEIGHT = 49.0;

POSITION_X = -MOUNT_WIDTH/2.0;
POSITION_Y = -MOUNT_HEIGHT/2.0;
LABEL = "BL - Pi 3";

$fn = 100;

length = 2;
width = 8;
height = 1;
FLU = 1.6; // Fundamental Lego Unit = 1.6 mm

M = 2.5;

TOTAL_HEIGHT = 3;
PEG_HEIGHT = (TOTAL_HEIGHT - 1) * 2 * FLU;
PEG_RADIUS = 0.75;

BRICK_WIDTH = 5.0 * FLU; // basic brick width

bricks_x = round(POSITION_X / BRICK_WIDTH);
bricks_y = round(POSITION_Y / BRICK_WIDTH);

OFFSET_X = POSITION_X - ((bricks_x + 0.5) * BRICK_WIDTH);
OFFSET_1_Y = POSITION_Y - (bricks_y * BRICK_WIDTH) - ( 3 * BRICK_WIDTH);
OFFSET_2_Y = - OFFSET_1_Y;

echo(OFFSET_1_Y * 2);



union(){

	difference()
	{
        union(){
            translate([OFFSET_X, OFFSET_1_Y, 0]) cylinder(r = 2, h = PEG_HEIGHT);
            translate([OFFSET_X, OFFSET_1_Y, FLU* 2]) cylinder(r1 = 3.3, r2=0, h = FLU* 2);
            translate([OFFSET_X, OFFSET_2_Y, 0]) cylinder(r = 2, h = PEG_HEIGHT);
            translate([OFFSET_X, OFFSET_2_Y, FLU* 2]) cylinder(r1 = 3.3, r2=0, h = FLU * 2);
            
            translate([-length*BRICK_WIDTH/2.0, -width*BRICK_WIDTH/2.0, 0])
                cube([length*BRICK_WIDTH, width*BRICK_WIDTH, FLU * 2]);
        }
		translate([OFFSET_X, OFFSET_1_Y,-1]) cylinder(r = (M/2)-0.05, h = PEG_HEIGHT+2);
        translate([OFFSET_X, OFFSET_2_Y,-1]) cylinder(r = (M/2)-0.05, h = PEG_HEIGHT+2);
	}
    /*
    translate([OFFSET_X, OFFSET_1_Y, 0])
        thread_in(M, PEG_HEIGHT);
    
    translate([OFFSET_X, OFFSET_2_Y, 0])
        thread_in(M, PEG_HEIGHT);*/
}








