module comparator_16bit(
    input [15:0] a,
    input [15:0] b,
    output gt,
    output lt,
    output eq
);

assign gt = (a > b);
assign lt = (a < b);
assign eq = (a == b);

endmodule