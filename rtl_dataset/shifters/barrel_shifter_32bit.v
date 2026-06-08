module barrel_shifter_32bit(
input [31:0] a,
input [4:0] shift,
output [31:0] y
);

assign y = a << shift;

endmodule