module left_shifter_16bit(
input [15:0] a,
output [15:0] y
);

assign y = a << 1;

endmodule