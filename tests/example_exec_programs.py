class PirProgram_5144210254368372785:

  def __init__(self):

    self.parameter_630 = self.Op("builtin.parameter", 630, input_types=[], output_types=[self.t_dtensor([192, 2, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_1.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_631 = self.Op("builtin.parameter", 631, input_types=[], output_types=[self.t_dtensor([192], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_1.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_632 = self.Op("builtin.parameter", 632, input_types=[], output_types=[self.t_dtensor([25, 75, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_2.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_633 = self.Op("builtin.parameter", 633, input_types=[], output_types=[self.t_dtensor([25], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_2.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_634 = self.Op("builtin.parameter", 634, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_1.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_635 = self.Op("builtin.parameter", 635, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_1.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_636 = self.Op("builtin.parameter", 636, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_1.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_637 = self.Op("builtin.parameter", 637, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_1.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_638 = self.Op("builtin.parameter", 638, input_types=[], output_types=[self.t_dtensor([64, 64, 9, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_3.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_639 = self.Op("builtin.parameter", 639, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_3.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_640 = self.Op("builtin.parameter", 640, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_2.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_641 = self.Op("builtin.parameter", 641, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_2.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_642 = self.Op("builtin.parameter", 642, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_2.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_643 = self.Op("builtin.parameter", 643, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_2.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_644 = self.Op("builtin.parameter", 644, input_types=[], output_types=[self.t_dtensor([64, 64, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_4.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_645 = self.Op("builtin.parameter", 645, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_4.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_646 = self.Op("builtin.parameter", 646, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_3.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_647 = self.Op("builtin.parameter", 647, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_3.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_648 = self.Op("builtin.parameter", 648, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_3.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_649 = self.Op("builtin.parameter", 649, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_3.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_650 = self.Op("builtin.parameter", 650, input_types=[], output_types=[self.t_dtensor([192, 64, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_5.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_651 = self.Op("builtin.parameter", 651, input_types=[], output_types=[self.t_dtensor([192], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_5.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_652 = self.Op("builtin.parameter", 652, input_types=[], output_types=[self.t_dtensor([25, 75, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_6.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_653 = self.Op("builtin.parameter", 653, input_types=[], output_types=[self.t_dtensor([25], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_6.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_654 = self.Op("builtin.parameter", 654, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_4.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_655 = self.Op("builtin.parameter", 655, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_4.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_656 = self.Op("builtin.parameter", 656, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_4.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_657 = self.Op("builtin.parameter", 657, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_4.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_658 = self.Op("builtin.parameter", 658, input_types=[], output_types=[self.t_dtensor([64, 64, 9, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_7.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_659 = self.Op("builtin.parameter", 659, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_7.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_660 = self.Op("builtin.parameter", 660, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_5.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_661 = self.Op("builtin.parameter", 661, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_5.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_662 = self.Op("builtin.parameter", 662, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_5.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_663 = self.Op("builtin.parameter", 663, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_5.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_664 = self.Op("builtin.parameter", 664, input_types=[], output_types=[self.t_dtensor([64, 64, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_8.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_665 = self.Op("builtin.parameter", 665, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_8.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_666 = self.Op("builtin.parameter", 666, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_6.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_667 = self.Op("builtin.parameter", 667, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_6.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_668 = self.Op("builtin.parameter", 668, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_6.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_669 = self.Op("builtin.parameter", 669, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_6.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_670 = self.Op("builtin.parameter", 670, input_types=[], output_types=[self.t_dtensor([192, 64, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_9.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_671 = self.Op("builtin.parameter", 671, input_types=[], output_types=[self.t_dtensor([192], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_9.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_672 = self.Op("builtin.parameter", 672, input_types=[], output_types=[self.t_dtensor([25, 75, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_10.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_673 = self.Op("builtin.parameter", 673, input_types=[], output_types=[self.t_dtensor([25], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_10.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_674 = self.Op("builtin.parameter", 674, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_7.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_675 = self.Op("builtin.parameter", 675, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_7.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_676 = self.Op("builtin.parameter", 676, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_7.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_677 = self.Op("builtin.parameter", 677, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_7.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_678 = self.Op("builtin.parameter", 678, input_types=[], output_types=[self.t_dtensor([64, 64, 9, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_11.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_679 = self.Op("builtin.parameter", 679, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_11.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_680 = self.Op("builtin.parameter", 680, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_8.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_681 = self.Op("builtin.parameter", 681, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_8.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_682 = self.Op("builtin.parameter", 682, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_8.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_683 = self.Op("builtin.parameter", 683, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_8.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_684 = self.Op("builtin.parameter", 684, input_types=[], output_types=[self.t_dtensor([64, 64, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_12.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_685 = self.Op("builtin.parameter", 685, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_12.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_686 = self.Op("builtin.parameter", 686, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_9.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_687 = self.Op("builtin.parameter", 687, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_9.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_688 = self.Op("builtin.parameter", 688, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_9.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_689 = self.Op("builtin.parameter", 689, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_9.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_690 = self.Op("builtin.parameter", 690, input_types=[], output_types=[self.t_dtensor([192, 64, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_13.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_691 = self.Op("builtin.parameter", 691, input_types=[], output_types=[self.t_dtensor([192], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_13.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_692 = self.Op("builtin.parameter", 692, input_types=[], output_types=[self.t_dtensor([25, 75, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_14.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_693 = self.Op("builtin.parameter", 693, input_types=[], output_types=[self.t_dtensor([25], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_14.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_694 = self.Op("builtin.parameter", 694, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_10.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_695 = self.Op("builtin.parameter", 695, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_10.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_696 = self.Op("builtin.parameter", 696, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_10.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_697 = self.Op("builtin.parameter", 697, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_10.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_698 = self.Op("builtin.parameter", 698, input_types=[], output_types=[self.t_dtensor([64, 64, 9, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_15.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_699 = self.Op("builtin.parameter", 699, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_15.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_700 = self.Op("builtin.parameter", 700, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_11.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_701 = self.Op("builtin.parameter", 701, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_11.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_702 = self.Op("builtin.parameter", 702, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_11.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_703 = self.Op("builtin.parameter", 703, input_types=[], output_types=[self.t_dtensor([64], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_11.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_704 = self.Op("builtin.parameter", 704, input_types=[], output_types=[self.t_dtensor([128, 64, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_16.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_705 = self.Op("builtin.parameter", 705, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_16.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_706 = self.Op("builtin.parameter", 706, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_12.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_707 = self.Op("builtin.parameter", 707, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_12.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_708 = self.Op("builtin.parameter", 708, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_12.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_709 = self.Op("builtin.parameter", 709, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_12.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_710 = self.Op("builtin.parameter", 710, input_types=[], output_types=[self.t_dtensor([384, 64, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_17.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_711 = self.Op("builtin.parameter", 711, input_types=[], output_types=[self.t_dtensor([384], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_17.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_712 = self.Op("builtin.parameter", 712, input_types=[], output_types=[self.t_dtensor([25, 75, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_18.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_713 = self.Op("builtin.parameter", 713, input_types=[], output_types=[self.t_dtensor([25], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_18.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_714 = self.Op("builtin.parameter", 714, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_13.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_715 = self.Op("builtin.parameter", 715, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_13.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_716 = self.Op("builtin.parameter", 716, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_13.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_717 = self.Op("builtin.parameter", 717, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_13.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_718 = self.Op("builtin.parameter", 718, input_types=[], output_types=[self.t_dtensor([128, 128, 9, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_19.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_719 = self.Op("builtin.parameter", 719, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_19.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_720 = self.Op("builtin.parameter", 720, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_14.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_721 = self.Op("builtin.parameter", 721, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_14.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_722 = self.Op("builtin.parameter", 722, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_14.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_723 = self.Op("builtin.parameter", 723, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_14.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_724 = self.Op("builtin.parameter", 724, input_types=[], output_types=[self.t_dtensor([128, 128, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_20.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_725 = self.Op("builtin.parameter", 725, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_20.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_726 = self.Op("builtin.parameter", 726, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_15.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_727 = self.Op("builtin.parameter", 727, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_15.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_728 = self.Op("builtin.parameter", 728, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_15.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_729 = self.Op("builtin.parameter", 729, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_15.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_730 = self.Op("builtin.parameter", 730, input_types=[], output_types=[self.t_dtensor([384, 128, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_21.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_731 = self.Op("builtin.parameter", 731, input_types=[], output_types=[self.t_dtensor([384], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_21.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_732 = self.Op("builtin.parameter", 732, input_types=[], output_types=[self.t_dtensor([25, 75, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_22.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_733 = self.Op("builtin.parameter", 733, input_types=[], output_types=[self.t_dtensor([25], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_22.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_734 = self.Op("builtin.parameter", 734, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_16.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_735 = self.Op("builtin.parameter", 735, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_16.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_736 = self.Op("builtin.parameter", 736, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_16.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_737 = self.Op("builtin.parameter", 737, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_16.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_738 = self.Op("builtin.parameter", 738, input_types=[], output_types=[self.t_dtensor([128, 128, 9, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_23.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_739 = self.Op("builtin.parameter", 739, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_23.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_740 = self.Op("builtin.parameter", 740, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_17.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_741 = self.Op("builtin.parameter", 741, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_17.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_742 = self.Op("builtin.parameter", 742, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_17.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_743 = self.Op("builtin.parameter", 743, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_17.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_744 = self.Op("builtin.parameter", 744, input_types=[], output_types=[self.t_dtensor([128, 128, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_24.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_745 = self.Op("builtin.parameter", 745, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_24.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_746 = self.Op("builtin.parameter", 746, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_18.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_747 = self.Op("builtin.parameter", 747, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_18.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_748 = self.Op("builtin.parameter", 748, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_18.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_749 = self.Op("builtin.parameter", 749, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_18.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_750 = self.Op("builtin.parameter", 750, input_types=[], output_types=[self.t_dtensor([384, 128, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_25.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_751 = self.Op("builtin.parameter", 751, input_types=[], output_types=[self.t_dtensor([384], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_25.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_752 = self.Op("builtin.parameter", 752, input_types=[], output_types=[self.t_dtensor([25, 75, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_26.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_753 = self.Op("builtin.parameter", 753, input_types=[], output_types=[self.t_dtensor([25], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_26.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_754 = self.Op("builtin.parameter", 754, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_19.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_755 = self.Op("builtin.parameter", 755, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_19.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_756 = self.Op("builtin.parameter", 756, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_19.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_757 = self.Op("builtin.parameter", 757, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_19.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_758 = self.Op("builtin.parameter", 758, input_types=[], output_types=[self.t_dtensor([128, 128, 9, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_27.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_759 = self.Op("builtin.parameter", 759, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_27.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_760 = self.Op("builtin.parameter", 760, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_20.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_761 = self.Op("builtin.parameter", 761, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_20.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_762 = self.Op("builtin.parameter", 762, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_20.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_763 = self.Op("builtin.parameter", 763, input_types=[], output_types=[self.t_dtensor([128], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_20.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_764 = self.Op("builtin.parameter", 764, input_types=[], output_types=[self.t_dtensor([256, 128, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_28.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_765 = self.Op("builtin.parameter", 765, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_28.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_766 = self.Op("builtin.parameter", 766, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_21.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_767 = self.Op("builtin.parameter", 767, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_21.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_768 = self.Op("builtin.parameter", 768, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_21.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_769 = self.Op("builtin.parameter", 769, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_21.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_770 = self.Op("builtin.parameter", 770, input_types=[], output_types=[self.t_dtensor([768, 128, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_29.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_771 = self.Op("builtin.parameter", 771, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_29.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_772 = self.Op("builtin.parameter", 772, input_types=[], output_types=[self.t_dtensor([25, 75, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_30.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_773 = self.Op("builtin.parameter", 773, input_types=[], output_types=[self.t_dtensor([25], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_30.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_774 = self.Op("builtin.parameter", 774, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_22.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_775 = self.Op("builtin.parameter", 775, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_22.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_776 = self.Op("builtin.parameter", 776, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_22.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_777 = self.Op("builtin.parameter", 777, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_22.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_778 = self.Op("builtin.parameter", 778, input_types=[], output_types=[self.t_dtensor([256, 256, 9, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_31.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_779 = self.Op("builtin.parameter", 779, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_31.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_780 = self.Op("builtin.parameter", 780, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_23.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_781 = self.Op("builtin.parameter", 781, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_23.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_782 = self.Op("builtin.parameter", 782, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_23.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_783 = self.Op("builtin.parameter", 783, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_23.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_784 = self.Op("builtin.parameter", 784, input_types=[], output_types=[self.t_dtensor([256, 256, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_32.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_785 = self.Op("builtin.parameter", 785, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_32.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_786 = self.Op("builtin.parameter", 786, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_24.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_787 = self.Op("builtin.parameter", 787, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_24.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_788 = self.Op("builtin.parameter", 788, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_24.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_789 = self.Op("builtin.parameter", 789, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_24.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_790 = self.Op("builtin.parameter", 790, input_types=[], output_types=[self.t_dtensor([768, 256, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_33.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_791 = self.Op("builtin.parameter", 791, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_33.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_792 = self.Op("builtin.parameter", 792, input_types=[], output_types=[self.t_dtensor([25, 75, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_34.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_793 = self.Op("builtin.parameter", 793, input_types=[], output_types=[self.t_dtensor([25], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_34.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_794 = self.Op("builtin.parameter", 794, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_25.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_795 = self.Op("builtin.parameter", 795, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_25.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_796 = self.Op("builtin.parameter", 796, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_25.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_797 = self.Op("builtin.parameter", 797, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_25.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_798 = self.Op("builtin.parameter", 798, input_types=[], output_types=[self.t_dtensor([256, 256, 9, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_35.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_799 = self.Op("builtin.parameter", 799, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_35.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_800 = self.Op("builtin.parameter", 800, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_26.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_801 = self.Op("builtin.parameter", 801, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_26.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_802 = self.Op("builtin.parameter", 802, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_26.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_803 = self.Op("builtin.parameter", 803, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_26.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_804 = self.Op("builtin.parameter", 804, input_types=[], output_types=[self.t_dtensor([256, 256, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_36.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_805 = self.Op("builtin.parameter", 805, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_36.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_806 = self.Op("builtin.parameter", 806, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_27.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_807 = self.Op("builtin.parameter", 807, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_27.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_808 = self.Op("builtin.parameter", 808, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_27.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_809 = self.Op("builtin.parameter", 809, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_27.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_810 = self.Op("builtin.parameter", 810, input_types=[], output_types=[self.t_dtensor([768, 256, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_37.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_811 = self.Op("builtin.parameter", 811, input_types=[], output_types=[self.t_dtensor([768], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_37.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_812 = self.Op("builtin.parameter", 812, input_types=[], output_types=[self.t_dtensor([25, 75, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_38.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_813 = self.Op("builtin.parameter", 813, input_types=[], output_types=[self.t_dtensor([25], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_38.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_814 = self.Op("builtin.parameter", 814, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_28.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_815 = self.Op("builtin.parameter", 815, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_28.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_816 = self.Op("builtin.parameter", 816, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_28.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_817 = self.Op("builtin.parameter", 817, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_28.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_818 = self.Op("builtin.parameter", 818, input_types=[], output_types=[self.t_dtensor([256, 256, 9, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_39.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_819 = self.Op("builtin.parameter", 819, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_39.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_820 = self.Op("builtin.parameter", 820, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_29.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_821 = self.Op("builtin.parameter", 821, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_29.w_1"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_822 = self.Op("builtin.parameter", 822, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_29.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_823 = self.Op("builtin.parameter", 823, input_types=[], output_types=[self.t_dtensor([256], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("batch_norm2d_29.w_2"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_824 = self.Op("builtin.parameter", 824, input_types=[], output_types=[self.t_dtensor([30, 256, 1, 1], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_40.w_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.parameter_825 = self.Op("builtin.parameter", 825, input_types=[], output_types=[self.t_dtensor([30], self.t_f32())], attrs={"persistable":self.a_array(self.a_bool(True)), "parameter_name":self.a_str("conv2d_40.b_0"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_826 = self.Op("pd_kernel.phi_kernel", 826, input_types=[], output_types=[self.t_dtensor([-1, 2, 350, 25, 1], self.t_f32())], attrs={"name":self.a_str("data_batch_0"), "col":self.a_i32(0), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.feed"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str(""), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_828 = self.Op("pd_kernel.phi_kernel", 828, input_types=[self.t_dtensor([-1, 2, 350, 25, 1], self.t_f32())], output_types=[self.t_dtensor([5], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.shape"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("shape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_829 = self.Op("pd_kernel.phi_kernel", 829, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(0)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_830 = self.Op("pd_kernel.phi_kernel", 830, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_831 = self.Op("pd_kernel.phi_kernel", 831, input_types=[self.t_dtensor([5], self.t_i32()), self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"axes":self.a_array(self.a_i64(0)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("slice"), "persistable":self.a_array(self.a_bool(False)), "infer_flags":self.a_array(self.a_i64(1)), "decrease_axis":self.a_array(self.a_i64(0)), "op_name":self.a_str("pd_op.slice"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_832 = self.Op("pd_kernel.phi_kernel", 832, input_types=[self.t_dtensor([-1, 2, 350, 25, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 1, 2, 350, 25], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(4), self.a_i32(1), self.a_i32(2), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_833 = self.Op("pd_kernel.phi_kernel", 833, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs={"place":self.a_place("cpu"), "kernel_key":self.a_kernel(), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(True)), "value":self.a_f64("1"), "kernel_name":self.a_str("full"), "dtype":self.a_dtype("float32"), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_834 = self.Op("pd_kernel.phi_kernel", 834, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"bias_after_scale":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "bias":self.a_f32("0"), "op_name":self.a_str("pd_op.scale"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("scale"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_835 = self.Op("pd_kernel.phi_kernel", 835, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("2"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_836 = self.Op("pd_kernel.phi_kernel", 836, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("350"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_837 = self.Op("pd_kernel.phi_kernel", 837, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("25"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_838 = self.Op("builtin.combine", 838, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_839 = self.Op("pd_kernel.phi_kernel", 839, input_types=[self.t_dtensor([-1, 1, 2, 350, 25], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 2, 350, 25], self.t_f32()), self.t_dtensor([0, -1, 1, 2, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_840 = self.Op("pd_kernel.phi_kernel", 840, input_types=[self.t_dtensor([-1, 2, 350, 25], self.t_f32()), self.t_dtensor([192, 2, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_841 = self.Op("pd_kernel.phi_kernel", 841, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(192), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_842 = self.Op("pd_kernel.phi_kernel", 842, input_types=[self.t_dtensor([192], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 192, 1, 1], self.t_f32()), self.t_dtensor([0, 192], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_843 = self.Op("pd_kernel.phi_kernel", 843, input_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32()), self.t_dtensor([1, 192, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_844 = self.Op("pd_kernel.phi_kernel", 844, input_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32())], output_types=[self.t_dtensor([4], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.shape"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("shape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_845 = self.Op("pd_kernel.phi_kernel", 845, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(0)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_846 = self.Op("pd_kernel.phi_kernel", 846, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_847 = self.Op("pd_kernel.phi_kernel", 847, input_types=[self.t_dtensor([4], self.t_i32()), self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"axes":self.a_array(self.a_i64(0)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("slice"), "persistable":self.a_array(self.a_bool(False)), "infer_flags":self.a_array(self.a_i64(1)), "decrease_axis":self.a_array(self.a_i64(0)), "op_name":self.a_str("pd_op.slice"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_848 = self.Op("pd_kernel.phi_kernel", 848, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("64"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_849 = self.Op("pd_kernel.phi_kernel", 849, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("3"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_850 = self.Op("pd_kernel.phi_kernel", 850, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("350"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_851 = self.Op("pd_kernel.phi_kernel", 851, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("25"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_852 = self.Op("builtin.combine", 852, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_853 = self.Op("pd_kernel.phi_kernel", 853, input_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 64, 3, 350, 25], self.t_f32()), self.t_dtensor([0, -1, 192, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_854 = self.Op("pd_kernel.phi_kernel", 854, input_types=[self.t_dtensor([-1, 64, 3, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 3, 25, 350], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(1), self.a_i32(2), self.a_i32(4), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_855 = self.Op("pd_kernel.phi_kernel", 855, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("64"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_856 = self.Op("pd_kernel.phi_kernel", 856, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("75"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_857 = self.Op("pd_kernel.phi_kernel", 857, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("350"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_858 = self.Op("builtin.combine", 858, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_859 = self.Op("pd_kernel.phi_kernel", 859, input_types=[self.t_dtensor([-1, 64, 3, 25, 350], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 64, 75, 350], self.t_f32()), self.t_dtensor([0, -1, 64, 3, 25, 350], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_860 = self.Op("pd_kernel.phi_kernel", 860, input_types=[self.t_dtensor([-1, 64, 75, 350], self.t_f32())], output_types=[self.t_dtensor([-1, 75, 64, 350], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_861 = self.Op("pd_kernel.phi_kernel", 861, input_types=[self.t_dtensor([-1, 75, 64, 350], self.t_f32()), self.t_dtensor([25, 75, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_862 = self.Op("pd_kernel.phi_kernel", 862, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(25), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_863 = self.Op("pd_kernel.phi_kernel", 863, input_types=[self.t_dtensor([25], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 25, 1, 1], self.t_f32()), self.t_dtensor([0, 25], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_864 = self.Op("pd_kernel.phi_kernel", 864, input_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32()), self.t_dtensor([1, 25, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_865 = self.Op("pd_kernel.phi_kernel", 865, input_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(3), self.a_i32(1)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_866 = self.Op("pd_kernel.phi_kernel", 866, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_867 = self.Op("pd_kernel.phi_kernel", 867, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_868 = self.Op("pd_kernel.phi_kernel", 868, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64, 64, 9, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(4), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_869 = self.Op("pd_kernel.phi_kernel", 869, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(64), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_870 = self.Op("pd_kernel.phi_kernel", 870, input_types=[self.t_dtensor([64], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 64, 1, 1], self.t_f32()), self.t_dtensor([0, 64], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_871 = self.Op("pd_kernel.phi_kernel", 871, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([1, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_872 = self.Op("pd_kernel.phi_kernel", 872, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_873 = self.Op("pd_kernel.phi_kernel", 873, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_874 = self.Op("pd_kernel.phi_kernel", 874, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_875 = self.Op("pd_kernel.phi_kernel", 875, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(64), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_876 = self.Op("pd_kernel.phi_kernel", 876, input_types=[self.t_dtensor([64], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 64, 1, 1], self.t_f32()), self.t_dtensor([0, 64], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_877 = self.Op("pd_kernel.phi_kernel", 877, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([1, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_878 = self.Op("pd_kernel.phi_kernel", 878, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_879 = self.Op("pd_kernel.phi_kernel", 879, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([192, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_880 = self.Op("pd_kernel.phi_kernel", 880, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(192), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_881 = self.Op("pd_kernel.phi_kernel", 881, input_types=[self.t_dtensor([192], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 192, 1, 1], self.t_f32()), self.t_dtensor([0, 192], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_882 = self.Op("pd_kernel.phi_kernel", 882, input_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32()), self.t_dtensor([1, 192, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_883 = self.Op("pd_kernel.phi_kernel", 883, input_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32())], output_types=[self.t_dtensor([4], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.shape"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("shape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_884 = self.Op("pd_kernel.phi_kernel", 884, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(0)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_885 = self.Op("pd_kernel.phi_kernel", 885, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_886 = self.Op("pd_kernel.phi_kernel", 886, input_types=[self.t_dtensor([4], self.t_i32()), self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"axes":self.a_array(self.a_i64(0)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("slice"), "persistable":self.a_array(self.a_bool(False)), "infer_flags":self.a_array(self.a_i64(1)), "decrease_axis":self.a_array(self.a_i64(0)), "op_name":self.a_str("pd_op.slice"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_887 = self.Op("pd_kernel.phi_kernel", 887, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("64"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_888 = self.Op("pd_kernel.phi_kernel", 888, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("3"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_889 = self.Op("pd_kernel.phi_kernel", 889, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("350"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_890 = self.Op("pd_kernel.phi_kernel", 890, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("25"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_891 = self.Op("builtin.combine", 891, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_892 = self.Op("pd_kernel.phi_kernel", 892, input_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 64, 3, 350, 25], self.t_f32()), self.t_dtensor([0, -1, 192, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_893 = self.Op("pd_kernel.phi_kernel", 893, input_types=[self.t_dtensor([-1, 64, 3, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 3, 25, 350], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(1), self.a_i32(2), self.a_i32(4), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_894 = self.Op("pd_kernel.phi_kernel", 894, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("64"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_895 = self.Op("pd_kernel.phi_kernel", 895, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("75"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_896 = self.Op("pd_kernel.phi_kernel", 896, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("350"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_897 = self.Op("builtin.combine", 897, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_898 = self.Op("pd_kernel.phi_kernel", 898, input_types=[self.t_dtensor([-1, 64, 3, 25, 350], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 64, 75, 350], self.t_f32()), self.t_dtensor([0, -1, 64, 3, 25, 350], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_899 = self.Op("pd_kernel.phi_kernel", 899, input_types=[self.t_dtensor([-1, 64, 75, 350], self.t_f32())], output_types=[self.t_dtensor([-1, 75, 64, 350], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_900 = self.Op("pd_kernel.phi_kernel", 900, input_types=[self.t_dtensor([-1, 75, 64, 350], self.t_f32()), self.t_dtensor([25, 75, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_901 = self.Op("pd_kernel.phi_kernel", 901, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(25), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_902 = self.Op("pd_kernel.phi_kernel", 902, input_types=[self.t_dtensor([25], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 25, 1, 1], self.t_f32()), self.t_dtensor([0, 25], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_903 = self.Op("pd_kernel.phi_kernel", 903, input_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32()), self.t_dtensor([1, 25, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_904 = self.Op("pd_kernel.phi_kernel", 904, input_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(3), self.a_i32(1)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_905 = self.Op("pd_kernel.phi_kernel", 905, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_906 = self.Op("pd_kernel.phi_kernel", 906, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_907 = self.Op("pd_kernel.phi_kernel", 907, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64, 64, 9, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(4), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_908 = self.Op("pd_kernel.phi_kernel", 908, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(64), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_909 = self.Op("pd_kernel.phi_kernel", 909, input_types=[self.t_dtensor([64], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 64, 1, 1], self.t_f32()), self.t_dtensor([0, 64], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_910 = self.Op("pd_kernel.phi_kernel", 910, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([1, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_911 = self.Op("pd_kernel.phi_kernel", 911, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_912 = self.Op("pd_kernel.phi_kernel", 912, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([-1, 64, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_913 = self.Op("pd_kernel.phi_kernel", 913, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_914 = self.Op("pd_kernel.phi_kernel", 914, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_915 = self.Op("pd_kernel.phi_kernel", 915, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(64), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_916 = self.Op("pd_kernel.phi_kernel", 916, input_types=[self.t_dtensor([64], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 64, 1, 1], self.t_f32()), self.t_dtensor([0, 64], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_917 = self.Op("pd_kernel.phi_kernel", 917, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([1, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_918 = self.Op("pd_kernel.phi_kernel", 918, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_919 = self.Op("pd_kernel.phi_kernel", 919, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([192, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_920 = self.Op("pd_kernel.phi_kernel", 920, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(192), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_921 = self.Op("pd_kernel.phi_kernel", 921, input_types=[self.t_dtensor([192], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 192, 1, 1], self.t_f32()), self.t_dtensor([0, 192], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_922 = self.Op("pd_kernel.phi_kernel", 922, input_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32()), self.t_dtensor([1, 192, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_923 = self.Op("pd_kernel.phi_kernel", 923, input_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32())], output_types=[self.t_dtensor([4], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.shape"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("shape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_924 = self.Op("pd_kernel.phi_kernel", 924, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(0)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_925 = self.Op("pd_kernel.phi_kernel", 925, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_926 = self.Op("pd_kernel.phi_kernel", 926, input_types=[self.t_dtensor([4], self.t_i32()), self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"axes":self.a_array(self.a_i64(0)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("slice"), "persistable":self.a_array(self.a_bool(False)), "infer_flags":self.a_array(self.a_i64(1)), "decrease_axis":self.a_array(self.a_i64(0)), "op_name":self.a_str("pd_op.slice"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_927 = self.Op("pd_kernel.phi_kernel", 927, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("64"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_928 = self.Op("pd_kernel.phi_kernel", 928, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("3"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_929 = self.Op("pd_kernel.phi_kernel", 929, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("350"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_930 = self.Op("pd_kernel.phi_kernel", 930, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("25"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_931 = self.Op("builtin.combine", 931, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_932 = self.Op("pd_kernel.phi_kernel", 932, input_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 64, 3, 350, 25], self.t_f32()), self.t_dtensor([0, -1, 192, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_933 = self.Op("pd_kernel.phi_kernel", 933, input_types=[self.t_dtensor([-1, 64, 3, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 3, 25, 350], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(1), self.a_i32(2), self.a_i32(4), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_934 = self.Op("pd_kernel.phi_kernel", 934, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("64"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_935 = self.Op("pd_kernel.phi_kernel", 935, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("75"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_936 = self.Op("pd_kernel.phi_kernel", 936, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("350"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_937 = self.Op("builtin.combine", 937, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_938 = self.Op("pd_kernel.phi_kernel", 938, input_types=[self.t_dtensor([-1, 64, 3, 25, 350], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 64, 75, 350], self.t_f32()), self.t_dtensor([0, -1, 64, 3, 25, 350], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_939 = self.Op("pd_kernel.phi_kernel", 939, input_types=[self.t_dtensor([-1, 64, 75, 350], self.t_f32())], output_types=[self.t_dtensor([-1, 75, 64, 350], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_940 = self.Op("pd_kernel.phi_kernel", 940, input_types=[self.t_dtensor([-1, 75, 64, 350], self.t_f32()), self.t_dtensor([25, 75, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_941 = self.Op("pd_kernel.phi_kernel", 941, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(25), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_942 = self.Op("pd_kernel.phi_kernel", 942, input_types=[self.t_dtensor([25], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 25, 1, 1], self.t_f32()), self.t_dtensor([0, 25], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_943 = self.Op("pd_kernel.phi_kernel", 943, input_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32()), self.t_dtensor([1, 25, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_944 = self.Op("pd_kernel.phi_kernel", 944, input_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(3), self.a_i32(1)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_945 = self.Op("pd_kernel.phi_kernel", 945, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_946 = self.Op("pd_kernel.phi_kernel", 946, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_947 = self.Op("pd_kernel.phi_kernel", 947, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64, 64, 9, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(4), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_948 = self.Op("pd_kernel.phi_kernel", 948, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(64), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_949 = self.Op("pd_kernel.phi_kernel", 949, input_types=[self.t_dtensor([64], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 64, 1, 1], self.t_f32()), self.t_dtensor([0, 64], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_950 = self.Op("pd_kernel.phi_kernel", 950, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([1, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_951 = self.Op("pd_kernel.phi_kernel", 951, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_952 = self.Op("pd_kernel.phi_kernel", 952, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([-1, 64, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_953 = self.Op("pd_kernel.phi_kernel", 953, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_954 = self.Op("pd_kernel.phi_kernel", 954, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_955 = self.Op("pd_kernel.phi_kernel", 955, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(64), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_956 = self.Op("pd_kernel.phi_kernel", 956, input_types=[self.t_dtensor([64], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 64, 1, 1], self.t_f32()), self.t_dtensor([0, 64], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_957 = self.Op("pd_kernel.phi_kernel", 957, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([1, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_958 = self.Op("pd_kernel.phi_kernel", 958, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_959 = self.Op("pd_kernel.phi_kernel", 959, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([192, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_960 = self.Op("pd_kernel.phi_kernel", 960, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(192), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_961 = self.Op("pd_kernel.phi_kernel", 961, input_types=[self.t_dtensor([192], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 192, 1, 1], self.t_f32()), self.t_dtensor([0, 192], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_962 = self.Op("pd_kernel.phi_kernel", 962, input_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32()), self.t_dtensor([1, 192, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_963 = self.Op("pd_kernel.phi_kernel", 963, input_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32())], output_types=[self.t_dtensor([4], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.shape"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("shape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_964 = self.Op("pd_kernel.phi_kernel", 964, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(0)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_965 = self.Op("pd_kernel.phi_kernel", 965, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_966 = self.Op("pd_kernel.phi_kernel", 966, input_types=[self.t_dtensor([4], self.t_i32()), self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"axes":self.a_array(self.a_i64(0)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("slice"), "persistable":self.a_array(self.a_bool(False)), "infer_flags":self.a_array(self.a_i64(1)), "decrease_axis":self.a_array(self.a_i64(0)), "op_name":self.a_str("pd_op.slice"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_967 = self.Op("pd_kernel.phi_kernel", 967, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("64"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_968 = self.Op("pd_kernel.phi_kernel", 968, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("3"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_969 = self.Op("pd_kernel.phi_kernel", 969, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("350"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_970 = self.Op("pd_kernel.phi_kernel", 970, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("25"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_971 = self.Op("builtin.combine", 971, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_972 = self.Op("pd_kernel.phi_kernel", 972, input_types=[self.t_dtensor([-1, 192, 350, 25], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 64, 3, 350, 25], self.t_f32()), self.t_dtensor([0, -1, 192, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_973 = self.Op("pd_kernel.phi_kernel", 973, input_types=[self.t_dtensor([-1, 64, 3, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 3, 25, 350], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(1), self.a_i32(2), self.a_i32(4), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_974 = self.Op("pd_kernel.phi_kernel", 974, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("64"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_975 = self.Op("pd_kernel.phi_kernel", 975, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("75"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_976 = self.Op("pd_kernel.phi_kernel", 976, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("350"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_977 = self.Op("builtin.combine", 977, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_978 = self.Op("pd_kernel.phi_kernel", 978, input_types=[self.t_dtensor([-1, 64, 3, 25, 350], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 64, 75, 350], self.t_f32()), self.t_dtensor([0, -1, 64, 3, 25, 350], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_979 = self.Op("pd_kernel.phi_kernel", 979, input_types=[self.t_dtensor([-1, 64, 75, 350], self.t_f32())], output_types=[self.t_dtensor([-1, 75, 64, 350], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_980 = self.Op("pd_kernel.phi_kernel", 980, input_types=[self.t_dtensor([-1, 75, 64, 350], self.t_f32()), self.t_dtensor([25, 75, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_981 = self.Op("pd_kernel.phi_kernel", 981, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(25), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_982 = self.Op("pd_kernel.phi_kernel", 982, input_types=[self.t_dtensor([25], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 25, 1, 1], self.t_f32()), self.t_dtensor([0, 25], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_983 = self.Op("pd_kernel.phi_kernel", 983, input_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32()), self.t_dtensor([1, 25, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_984 = self.Op("pd_kernel.phi_kernel", 984, input_types=[self.t_dtensor([-1, 25, 64, 350], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(3), self.a_i32(1)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_985 = self.Op("pd_kernel.phi_kernel", 985, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_986 = self.Op("pd_kernel.phi_kernel", 986, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_987 = self.Op("pd_kernel.phi_kernel", 987, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64, 64, 9, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(4), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_988 = self.Op("pd_kernel.phi_kernel", 988, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(64), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_989 = self.Op("pd_kernel.phi_kernel", 989, input_types=[self.t_dtensor([64], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 64, 1, 1], self.t_f32()), self.t_dtensor([0, 64], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_990 = self.Op("pd_kernel.phi_kernel", 990, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([1, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_991 = self.Op("pd_kernel.phi_kernel", 991, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([64], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_992 = self.Op("pd_kernel.phi_kernel", 992, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([-1, 64, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_993 = self.Op("pd_kernel.phi_kernel", 993, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_994 = self.Op("pd_kernel.phi_kernel", 994, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([128, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(2), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_995 = self.Op("pd_kernel.phi_kernel", 995, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(128), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_996 = self.Op("pd_kernel.phi_kernel", 996, input_types=[self.t_dtensor([128], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 128, 1, 1], self.t_f32()), self.t_dtensor([0, 128], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_997 = self.Op("pd_kernel.phi_kernel", 997, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([1, 128, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_998 = self.Op("pd_kernel.phi_kernel", 998, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_999 = self.Op("pd_kernel.phi_kernel", 999, input_types=[self.t_dtensor([-1, 64, 350, 25], self.t_f32()), self.t_dtensor([384, 64, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 384, 350, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1000 = self.Op("pd_kernel.phi_kernel", 1000, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(384), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1001 = self.Op("pd_kernel.phi_kernel", 1001, input_types=[self.t_dtensor([384], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 384, 1, 1], self.t_f32()), self.t_dtensor([0, 384], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1002 = self.Op("pd_kernel.phi_kernel", 1002, input_types=[self.t_dtensor([-1, 384, 350, 25], self.t_f32()), self.t_dtensor([1, 384, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 384, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1003 = self.Op("pd_kernel.phi_kernel", 1003, input_types=[self.t_dtensor([-1, 384, 350, 25], self.t_f32())], output_types=[self.t_dtensor([4], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.shape"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("shape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1004 = self.Op("pd_kernel.phi_kernel", 1004, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(0)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1005 = self.Op("pd_kernel.phi_kernel", 1005, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1006 = self.Op("pd_kernel.phi_kernel", 1006, input_types=[self.t_dtensor([4], self.t_i32()), self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"axes":self.a_array(self.a_i64(0)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("slice"), "persistable":self.a_array(self.a_bool(False)), "infer_flags":self.a_array(self.a_i64(1)), "decrease_axis":self.a_array(self.a_i64(0)), "op_name":self.a_str("pd_op.slice"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1007 = self.Op("pd_kernel.phi_kernel", 1007, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("128"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1008 = self.Op("pd_kernel.phi_kernel", 1008, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("3"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1009 = self.Op("pd_kernel.phi_kernel", 1009, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("350"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1010 = self.Op("pd_kernel.phi_kernel", 1010, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("25"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1011 = self.Op("builtin.combine", 1011, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1012 = self.Op("pd_kernel.phi_kernel", 1012, input_types=[self.t_dtensor([-1, 384, 350, 25], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 128, 3, 350, 25], self.t_f32()), self.t_dtensor([0, -1, 384, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1013 = self.Op("pd_kernel.phi_kernel", 1013, input_types=[self.t_dtensor([-1, 128, 3, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 3, 25, 350], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(1), self.a_i32(2), self.a_i32(4), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1014 = self.Op("pd_kernel.phi_kernel", 1014, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("128"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1015 = self.Op("pd_kernel.phi_kernel", 1015, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("75"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1016 = self.Op("pd_kernel.phi_kernel", 1016, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("350"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1017 = self.Op("builtin.combine", 1017, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1018 = self.Op("pd_kernel.phi_kernel", 1018, input_types=[self.t_dtensor([-1, 128, 3, 25, 350], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 128, 75, 350], self.t_f32()), self.t_dtensor([0, -1, 128, 3, 25, 350], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1019 = self.Op("pd_kernel.phi_kernel", 1019, input_types=[self.t_dtensor([-1, 128, 75, 350], self.t_f32())], output_types=[self.t_dtensor([-1, 75, 128, 350], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1020 = self.Op("pd_kernel.phi_kernel", 1020, input_types=[self.t_dtensor([-1, 75, 128, 350], self.t_f32()), self.t_dtensor([25, 75, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 128, 350], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1021 = self.Op("pd_kernel.phi_kernel", 1021, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(25), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1022 = self.Op("pd_kernel.phi_kernel", 1022, input_types=[self.t_dtensor([25], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 25, 1, 1], self.t_f32()), self.t_dtensor([0, 25], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1023 = self.Op("pd_kernel.phi_kernel", 1023, input_types=[self.t_dtensor([-1, 25, 128, 350], self.t_f32()), self.t_dtensor([1, 25, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 128, 350], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1024 = self.Op("pd_kernel.phi_kernel", 1024, input_types=[self.t_dtensor([-1, 25, 128, 350], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 350, 25], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(3), self.a_i32(1)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1025 = self.Op("pd_kernel.phi_kernel", 1025, input_types=[self.t_dtensor([-1, 128, 350, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 350, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1026 = self.Op("pd_kernel.phi_kernel", 1026, input_types=[self.t_dtensor([-1, 128, 350, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 350, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1027 = self.Op("pd_kernel.phi_kernel", 1027, input_types=[self.t_dtensor([-1, 128, 350, 25], self.t_f32()), self.t_dtensor([128, 128, 9, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(2), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(4), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1028 = self.Op("pd_kernel.phi_kernel", 1028, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(128), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1029 = self.Op("pd_kernel.phi_kernel", 1029, input_types=[self.t_dtensor([128], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 128, 1, 1], self.t_f32()), self.t_dtensor([0, 128], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1030 = self.Op("pd_kernel.phi_kernel", 1030, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([1, 128, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1031 = self.Op("pd_kernel.phi_kernel", 1031, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1032 = self.Op("pd_kernel.phi_kernel", 1032, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([-1, 128, 175, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1033 = self.Op("pd_kernel.phi_kernel", 1033, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1034 = self.Op("pd_kernel.phi_kernel", 1034, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128, 128, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1035 = self.Op("pd_kernel.phi_kernel", 1035, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(128), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1036 = self.Op("pd_kernel.phi_kernel", 1036, input_types=[self.t_dtensor([128], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 128, 1, 1], self.t_f32()), self.t_dtensor([0, 128], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1037 = self.Op("pd_kernel.phi_kernel", 1037, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([1, 128, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1038 = self.Op("pd_kernel.phi_kernel", 1038, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1039 = self.Op("pd_kernel.phi_kernel", 1039, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([384, 128, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 384, 175, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1040 = self.Op("pd_kernel.phi_kernel", 1040, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(384), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1041 = self.Op("pd_kernel.phi_kernel", 1041, input_types=[self.t_dtensor([384], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 384, 1, 1], self.t_f32()), self.t_dtensor([0, 384], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1042 = self.Op("pd_kernel.phi_kernel", 1042, input_types=[self.t_dtensor([-1, 384, 175, 25], self.t_f32()), self.t_dtensor([1, 384, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 384, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1043 = self.Op("pd_kernel.phi_kernel", 1043, input_types=[self.t_dtensor([-1, 384, 175, 25], self.t_f32())], output_types=[self.t_dtensor([4], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.shape"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("shape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1044 = self.Op("pd_kernel.phi_kernel", 1044, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(0)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1045 = self.Op("pd_kernel.phi_kernel", 1045, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1046 = self.Op("pd_kernel.phi_kernel", 1046, input_types=[self.t_dtensor([4], self.t_i32()), self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"axes":self.a_array(self.a_i64(0)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("slice"), "persistable":self.a_array(self.a_bool(False)), "infer_flags":self.a_array(self.a_i64(1)), "decrease_axis":self.a_array(self.a_i64(0)), "op_name":self.a_str("pd_op.slice"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1047 = self.Op("pd_kernel.phi_kernel", 1047, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("128"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1048 = self.Op("pd_kernel.phi_kernel", 1048, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("3"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1049 = self.Op("pd_kernel.phi_kernel", 1049, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("175"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1050 = self.Op("pd_kernel.phi_kernel", 1050, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("25"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1051 = self.Op("builtin.combine", 1051, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1052 = self.Op("pd_kernel.phi_kernel", 1052, input_types=[self.t_dtensor([-1, 384, 175, 25], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 128, 3, 175, 25], self.t_f32()), self.t_dtensor([0, -1, 384, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1053 = self.Op("pd_kernel.phi_kernel", 1053, input_types=[self.t_dtensor([-1, 128, 3, 175, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 3, 25, 175], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(1), self.a_i32(2), self.a_i32(4), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1054 = self.Op("pd_kernel.phi_kernel", 1054, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("128"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1055 = self.Op("pd_kernel.phi_kernel", 1055, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("75"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1056 = self.Op("pd_kernel.phi_kernel", 1056, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("175"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1057 = self.Op("builtin.combine", 1057, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1058 = self.Op("pd_kernel.phi_kernel", 1058, input_types=[self.t_dtensor([-1, 128, 3, 25, 175], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 128, 75, 175], self.t_f32()), self.t_dtensor([0, -1, 128, 3, 25, 175], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1059 = self.Op("pd_kernel.phi_kernel", 1059, input_types=[self.t_dtensor([-1, 128, 75, 175], self.t_f32())], output_types=[self.t_dtensor([-1, 75, 128, 175], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1060 = self.Op("pd_kernel.phi_kernel", 1060, input_types=[self.t_dtensor([-1, 75, 128, 175], self.t_f32()), self.t_dtensor([25, 75, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 128, 175], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1061 = self.Op("pd_kernel.phi_kernel", 1061, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(25), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1062 = self.Op("pd_kernel.phi_kernel", 1062, input_types=[self.t_dtensor([25], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 25, 1, 1], self.t_f32()), self.t_dtensor([0, 25], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1063 = self.Op("pd_kernel.phi_kernel", 1063, input_types=[self.t_dtensor([-1, 25, 128, 175], self.t_f32()), self.t_dtensor([1, 25, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 128, 175], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1064 = self.Op("pd_kernel.phi_kernel", 1064, input_types=[self.t_dtensor([-1, 25, 128, 175], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(3), self.a_i32(1)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1065 = self.Op("pd_kernel.phi_kernel", 1065, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1066 = self.Op("pd_kernel.phi_kernel", 1066, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1067 = self.Op("pd_kernel.phi_kernel", 1067, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128, 128, 9, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(4), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1068 = self.Op("pd_kernel.phi_kernel", 1068, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(128), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1069 = self.Op("pd_kernel.phi_kernel", 1069, input_types=[self.t_dtensor([128], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 128, 1, 1], self.t_f32()), self.t_dtensor([0, 128], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1070 = self.Op("pd_kernel.phi_kernel", 1070, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([1, 128, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1071 = self.Op("pd_kernel.phi_kernel", 1071, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1072 = self.Op("pd_kernel.phi_kernel", 1072, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([-1, 128, 175, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1073 = self.Op("pd_kernel.phi_kernel", 1073, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1074 = self.Op("pd_kernel.phi_kernel", 1074, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128, 128, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1075 = self.Op("pd_kernel.phi_kernel", 1075, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(128), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1076 = self.Op("pd_kernel.phi_kernel", 1076, input_types=[self.t_dtensor([128], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 128, 1, 1], self.t_f32()), self.t_dtensor([0, 128], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1077 = self.Op("pd_kernel.phi_kernel", 1077, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([1, 128, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1078 = self.Op("pd_kernel.phi_kernel", 1078, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1079 = self.Op("pd_kernel.phi_kernel", 1079, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([384, 128, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 384, 175, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1080 = self.Op("pd_kernel.phi_kernel", 1080, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(384), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1081 = self.Op("pd_kernel.phi_kernel", 1081, input_types=[self.t_dtensor([384], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 384, 1, 1], self.t_f32()), self.t_dtensor([0, 384], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1082 = self.Op("pd_kernel.phi_kernel", 1082, input_types=[self.t_dtensor([-1, 384, 175, 25], self.t_f32()), self.t_dtensor([1, 384, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 384, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1083 = self.Op("pd_kernel.phi_kernel", 1083, input_types=[self.t_dtensor([-1, 384, 175, 25], self.t_f32())], output_types=[self.t_dtensor([4], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.shape"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("shape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1084 = self.Op("pd_kernel.phi_kernel", 1084, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(0)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1085 = self.Op("pd_kernel.phi_kernel", 1085, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1086 = self.Op("pd_kernel.phi_kernel", 1086, input_types=[self.t_dtensor([4], self.t_i32()), self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"axes":self.a_array(self.a_i64(0)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("slice"), "persistable":self.a_array(self.a_bool(False)), "infer_flags":self.a_array(self.a_i64(1)), "decrease_axis":self.a_array(self.a_i64(0)), "op_name":self.a_str("pd_op.slice"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1087 = self.Op("pd_kernel.phi_kernel", 1087, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("128"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1088 = self.Op("pd_kernel.phi_kernel", 1088, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("3"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1089 = self.Op("pd_kernel.phi_kernel", 1089, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("175"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1090 = self.Op("pd_kernel.phi_kernel", 1090, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("25"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1091 = self.Op("builtin.combine", 1091, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1092 = self.Op("pd_kernel.phi_kernel", 1092, input_types=[self.t_dtensor([-1, 384, 175, 25], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 128, 3, 175, 25], self.t_f32()), self.t_dtensor([0, -1, 384, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1093 = self.Op("pd_kernel.phi_kernel", 1093, input_types=[self.t_dtensor([-1, 128, 3, 175, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 3, 25, 175], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(1), self.a_i32(2), self.a_i32(4), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1094 = self.Op("pd_kernel.phi_kernel", 1094, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("128"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1095 = self.Op("pd_kernel.phi_kernel", 1095, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("75"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1096 = self.Op("pd_kernel.phi_kernel", 1096, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("175"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1097 = self.Op("builtin.combine", 1097, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1098 = self.Op("pd_kernel.phi_kernel", 1098, input_types=[self.t_dtensor([-1, 128, 3, 25, 175], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 128, 75, 175], self.t_f32()), self.t_dtensor([0, -1, 128, 3, 25, 175], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1099 = self.Op("pd_kernel.phi_kernel", 1099, input_types=[self.t_dtensor([-1, 128, 75, 175], self.t_f32())], output_types=[self.t_dtensor([-1, 75, 128, 175], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1100 = self.Op("pd_kernel.phi_kernel", 1100, input_types=[self.t_dtensor([-1, 75, 128, 175], self.t_f32()), self.t_dtensor([25, 75, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 128, 175], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1101 = self.Op("pd_kernel.phi_kernel", 1101, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(25), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1102 = self.Op("pd_kernel.phi_kernel", 1102, input_types=[self.t_dtensor([25], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 25, 1, 1], self.t_f32()), self.t_dtensor([0, 25], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1103 = self.Op("pd_kernel.phi_kernel", 1103, input_types=[self.t_dtensor([-1, 25, 128, 175], self.t_f32()), self.t_dtensor([1, 25, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 128, 175], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1104 = self.Op("pd_kernel.phi_kernel", 1104, input_types=[self.t_dtensor([-1, 25, 128, 175], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(3), self.a_i32(1)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1105 = self.Op("pd_kernel.phi_kernel", 1105, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1106 = self.Op("pd_kernel.phi_kernel", 1106, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1107 = self.Op("pd_kernel.phi_kernel", 1107, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128, 128, 9, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(4), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1108 = self.Op("pd_kernel.phi_kernel", 1108, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(128), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1109 = self.Op("pd_kernel.phi_kernel", 1109, input_types=[self.t_dtensor([128], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 128, 1, 1], self.t_f32()), self.t_dtensor([0, 128], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1110 = self.Op("pd_kernel.phi_kernel", 1110, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([1, 128, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1111 = self.Op("pd_kernel.phi_kernel", 1111, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([128], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1112 = self.Op("pd_kernel.phi_kernel", 1112, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([-1, 128, 175, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1113 = self.Op("pd_kernel.phi_kernel", 1113, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1114 = self.Op("pd_kernel.phi_kernel", 1114, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([256, 128, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(2), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1115 = self.Op("pd_kernel.phi_kernel", 1115, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(256), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1116 = self.Op("pd_kernel.phi_kernel", 1116, input_types=[self.t_dtensor([256], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 256, 1, 1], self.t_f32()), self.t_dtensor([0, 256], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1117 = self.Op("pd_kernel.phi_kernel", 1117, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([1, 256, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1118 = self.Op("pd_kernel.phi_kernel", 1118, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1119 = self.Op("pd_kernel.phi_kernel", 1119, input_types=[self.t_dtensor([-1, 128, 175, 25], self.t_f32()), self.t_dtensor([768, 128, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 768, 175, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1120 = self.Op("pd_kernel.phi_kernel", 1120, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(768), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1121 = self.Op("pd_kernel.phi_kernel", 1121, input_types=[self.t_dtensor([768], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 768, 1, 1], self.t_f32()), self.t_dtensor([0, 768], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1122 = self.Op("pd_kernel.phi_kernel", 1122, input_types=[self.t_dtensor([-1, 768, 175, 25], self.t_f32()), self.t_dtensor([1, 768, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 768, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1123 = self.Op("pd_kernel.phi_kernel", 1123, input_types=[self.t_dtensor([-1, 768, 175, 25], self.t_f32())], output_types=[self.t_dtensor([4], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.shape"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("shape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1124 = self.Op("pd_kernel.phi_kernel", 1124, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(0)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1125 = self.Op("pd_kernel.phi_kernel", 1125, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1126 = self.Op("pd_kernel.phi_kernel", 1126, input_types=[self.t_dtensor([4], self.t_i32()), self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"axes":self.a_array(self.a_i64(0)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("slice"), "persistable":self.a_array(self.a_bool(False)), "infer_flags":self.a_array(self.a_i64(1)), "decrease_axis":self.a_array(self.a_i64(0)), "op_name":self.a_str("pd_op.slice"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1127 = self.Op("pd_kernel.phi_kernel", 1127, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("256"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1128 = self.Op("pd_kernel.phi_kernel", 1128, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("3"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1129 = self.Op("pd_kernel.phi_kernel", 1129, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("175"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1130 = self.Op("pd_kernel.phi_kernel", 1130, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("25"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1131 = self.Op("builtin.combine", 1131, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1132 = self.Op("pd_kernel.phi_kernel", 1132, input_types=[self.t_dtensor([-1, 768, 175, 25], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 256, 3, 175, 25], self.t_f32()), self.t_dtensor([0, -1, 768, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1133 = self.Op("pd_kernel.phi_kernel", 1133, input_types=[self.t_dtensor([-1, 256, 3, 175, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 3, 25, 175], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(1), self.a_i32(2), self.a_i32(4), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1134 = self.Op("pd_kernel.phi_kernel", 1134, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("256"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1135 = self.Op("pd_kernel.phi_kernel", 1135, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("75"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1136 = self.Op("pd_kernel.phi_kernel", 1136, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("175"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1137 = self.Op("builtin.combine", 1137, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1138 = self.Op("pd_kernel.phi_kernel", 1138, input_types=[self.t_dtensor([-1, 256, 3, 25, 175], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 256, 75, 175], self.t_f32()), self.t_dtensor([0, -1, 256, 3, 25, 175], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1139 = self.Op("pd_kernel.phi_kernel", 1139, input_types=[self.t_dtensor([-1, 256, 75, 175], self.t_f32())], output_types=[self.t_dtensor([-1, 75, 256, 175], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1140 = self.Op("pd_kernel.phi_kernel", 1140, input_types=[self.t_dtensor([-1, 75, 256, 175], self.t_f32()), self.t_dtensor([25, 75, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 256, 175], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1141 = self.Op("pd_kernel.phi_kernel", 1141, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(25), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1142 = self.Op("pd_kernel.phi_kernel", 1142, input_types=[self.t_dtensor([25], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 25, 1, 1], self.t_f32()), self.t_dtensor([0, 25], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1143 = self.Op("pd_kernel.phi_kernel", 1143, input_types=[self.t_dtensor([-1, 25, 256, 175], self.t_f32()), self.t_dtensor([1, 25, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 256, 175], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1144 = self.Op("pd_kernel.phi_kernel", 1144, input_types=[self.t_dtensor([-1, 25, 256, 175], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 175, 25], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(3), self.a_i32(1)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1145 = self.Op("pd_kernel.phi_kernel", 1145, input_types=[self.t_dtensor([-1, 256, 175, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 175, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1146 = self.Op("pd_kernel.phi_kernel", 1146, input_types=[self.t_dtensor([-1, 256, 175, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 175, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1147 = self.Op("pd_kernel.phi_kernel", 1147, input_types=[self.t_dtensor([-1, 256, 175, 25], self.t_f32()), self.t_dtensor([256, 256, 9, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(2), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(4), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1148 = self.Op("pd_kernel.phi_kernel", 1148, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(256), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1149 = self.Op("pd_kernel.phi_kernel", 1149, input_types=[self.t_dtensor([256], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 256, 1, 1], self.t_f32()), self.t_dtensor([0, 256], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1150 = self.Op("pd_kernel.phi_kernel", 1150, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([1, 256, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1151 = self.Op("pd_kernel.phi_kernel", 1151, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1152 = self.Op("pd_kernel.phi_kernel", 1152, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([-1, 256, 88, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1153 = self.Op("pd_kernel.phi_kernel", 1153, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1154 = self.Op("pd_kernel.phi_kernel", 1154, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256, 256, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1155 = self.Op("pd_kernel.phi_kernel", 1155, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(256), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1156 = self.Op("pd_kernel.phi_kernel", 1156, input_types=[self.t_dtensor([256], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 256, 1, 1], self.t_f32()), self.t_dtensor([0, 256], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1157 = self.Op("pd_kernel.phi_kernel", 1157, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([1, 256, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1158 = self.Op("pd_kernel.phi_kernel", 1158, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1159 = self.Op("pd_kernel.phi_kernel", 1159, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([768, 256, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 768, 88, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1160 = self.Op("pd_kernel.phi_kernel", 1160, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(768), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1161 = self.Op("pd_kernel.phi_kernel", 1161, input_types=[self.t_dtensor([768], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 768, 1, 1], self.t_f32()), self.t_dtensor([0, 768], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1162 = self.Op("pd_kernel.phi_kernel", 1162, input_types=[self.t_dtensor([-1, 768, 88, 25], self.t_f32()), self.t_dtensor([1, 768, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 768, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1163 = self.Op("pd_kernel.phi_kernel", 1163, input_types=[self.t_dtensor([-1, 768, 88, 25], self.t_f32())], output_types=[self.t_dtensor([4], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.shape"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("shape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1164 = self.Op("pd_kernel.phi_kernel", 1164, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(0)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1165 = self.Op("pd_kernel.phi_kernel", 1165, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1166 = self.Op("pd_kernel.phi_kernel", 1166, input_types=[self.t_dtensor([4], self.t_i32()), self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"axes":self.a_array(self.a_i64(0)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("slice"), "persistable":self.a_array(self.a_bool(False)), "infer_flags":self.a_array(self.a_i64(1)), "decrease_axis":self.a_array(self.a_i64(0)), "op_name":self.a_str("pd_op.slice"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1167 = self.Op("pd_kernel.phi_kernel", 1167, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("256"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1168 = self.Op("pd_kernel.phi_kernel", 1168, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("3"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1169 = self.Op("pd_kernel.phi_kernel", 1169, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("88"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1170 = self.Op("pd_kernel.phi_kernel", 1170, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("25"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1171 = self.Op("builtin.combine", 1171, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1172 = self.Op("pd_kernel.phi_kernel", 1172, input_types=[self.t_dtensor([-1, 768, 88, 25], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 256, 3, 88, 25], self.t_f32()), self.t_dtensor([0, -1, 768, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1173 = self.Op("pd_kernel.phi_kernel", 1173, input_types=[self.t_dtensor([-1, 256, 3, 88, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 3, 25, 88], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(1), self.a_i32(2), self.a_i32(4), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1174 = self.Op("pd_kernel.phi_kernel", 1174, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("256"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1175 = self.Op("pd_kernel.phi_kernel", 1175, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("75"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1176 = self.Op("pd_kernel.phi_kernel", 1176, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("88"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1177 = self.Op("builtin.combine", 1177, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1178 = self.Op("pd_kernel.phi_kernel", 1178, input_types=[self.t_dtensor([-1, 256, 3, 25, 88], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 256, 75, 88], self.t_f32()), self.t_dtensor([0, -1, 256, 3, 25, 88], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1179 = self.Op("pd_kernel.phi_kernel", 1179, input_types=[self.t_dtensor([-1, 256, 75, 88], self.t_f32())], output_types=[self.t_dtensor([-1, 75, 256, 88], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1180 = self.Op("pd_kernel.phi_kernel", 1180, input_types=[self.t_dtensor([-1, 75, 256, 88], self.t_f32()), self.t_dtensor([25, 75, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 256, 88], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1181 = self.Op("pd_kernel.phi_kernel", 1181, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(25), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1182 = self.Op("pd_kernel.phi_kernel", 1182, input_types=[self.t_dtensor([25], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 25, 1, 1], self.t_f32()), self.t_dtensor([0, 25], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1183 = self.Op("pd_kernel.phi_kernel", 1183, input_types=[self.t_dtensor([-1, 25, 256, 88], self.t_f32()), self.t_dtensor([1, 25, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 256, 88], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1184 = self.Op("pd_kernel.phi_kernel", 1184, input_types=[self.t_dtensor([-1, 25, 256, 88], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(3), self.a_i32(1)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1185 = self.Op("pd_kernel.phi_kernel", 1185, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1186 = self.Op("pd_kernel.phi_kernel", 1186, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1187 = self.Op("pd_kernel.phi_kernel", 1187, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256, 256, 9, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(4), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1188 = self.Op("pd_kernel.phi_kernel", 1188, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(256), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1189 = self.Op("pd_kernel.phi_kernel", 1189, input_types=[self.t_dtensor([256], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 256, 1, 1], self.t_f32()), self.t_dtensor([0, 256], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1190 = self.Op("pd_kernel.phi_kernel", 1190, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([1, 256, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1191 = self.Op("pd_kernel.phi_kernel", 1191, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1192 = self.Op("pd_kernel.phi_kernel", 1192, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([-1, 256, 88, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1193 = self.Op("pd_kernel.phi_kernel", 1193, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1194 = self.Op("pd_kernel.phi_kernel", 1194, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256, 256, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1195 = self.Op("pd_kernel.phi_kernel", 1195, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(256), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1196 = self.Op("pd_kernel.phi_kernel", 1196, input_types=[self.t_dtensor([256], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 256, 1, 1], self.t_f32()), self.t_dtensor([0, 256], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1197 = self.Op("pd_kernel.phi_kernel", 1197, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([1, 256, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1198 = self.Op("pd_kernel.phi_kernel", 1198, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1199 = self.Op("pd_kernel.phi_kernel", 1199, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([768, 256, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 768, 88, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1200 = self.Op("pd_kernel.phi_kernel", 1200, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(768), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1201 = self.Op("pd_kernel.phi_kernel", 1201, input_types=[self.t_dtensor([768], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 768, 1, 1], self.t_f32()), self.t_dtensor([0, 768], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1202 = self.Op("pd_kernel.phi_kernel", 1202, input_types=[self.t_dtensor([-1, 768, 88, 25], self.t_f32()), self.t_dtensor([1, 768, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 768, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1203 = self.Op("pd_kernel.phi_kernel", 1203, input_types=[self.t_dtensor([-1, 768, 88, 25], self.t_f32())], output_types=[self.t_dtensor([4], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.shape"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("shape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1204 = self.Op("pd_kernel.phi_kernel", 1204, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(0)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1205 = self.Op("pd_kernel.phi_kernel", 1205, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1206 = self.Op("pd_kernel.phi_kernel", 1206, input_types=[self.t_dtensor([4], self.t_i32()), self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"axes":self.a_array(self.a_i64(0)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("slice"), "persistable":self.a_array(self.a_bool(False)), "infer_flags":self.a_array(self.a_i64(1)), "decrease_axis":self.a_array(self.a_i64(0)), "op_name":self.a_str("pd_op.slice"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1207 = self.Op("pd_kernel.phi_kernel", 1207, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("256"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1208 = self.Op("pd_kernel.phi_kernel", 1208, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("3"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1209 = self.Op("pd_kernel.phi_kernel", 1209, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("88"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1210 = self.Op("pd_kernel.phi_kernel", 1210, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("25"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1211 = self.Op("builtin.combine", 1211, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1212 = self.Op("pd_kernel.phi_kernel", 1212, input_types=[self.t_dtensor([-1, 768, 88, 25], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 256, 3, 88, 25], self.t_f32()), self.t_dtensor([0, -1, 768, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1213 = self.Op("pd_kernel.phi_kernel", 1213, input_types=[self.t_dtensor([-1, 256, 3, 88, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 3, 25, 88], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(1), self.a_i32(2), self.a_i32(4), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1214 = self.Op("pd_kernel.phi_kernel", 1214, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("256"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1215 = self.Op("pd_kernel.phi_kernel", 1215, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("75"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1216 = self.Op("pd_kernel.phi_kernel", 1216, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("88"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1217 = self.Op("builtin.combine", 1217, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1218 = self.Op("pd_kernel.phi_kernel", 1218, input_types=[self.t_dtensor([-1, 256, 3, 25, 88], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 256, 75, 88], self.t_f32()), self.t_dtensor([0, -1, 256, 3, 25, 88], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1219 = self.Op("pd_kernel.phi_kernel", 1219, input_types=[self.t_dtensor([-1, 256, 75, 88], self.t_f32())], output_types=[self.t_dtensor([-1, 75, 256, 88], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(1), self.a_i32(3)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1220 = self.Op("pd_kernel.phi_kernel", 1220, input_types=[self.t_dtensor([-1, 75, 256, 88], self.t_f32()), self.t_dtensor([25, 75, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 256, 88], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1221 = self.Op("pd_kernel.phi_kernel", 1221, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(25), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1222 = self.Op("pd_kernel.phi_kernel", 1222, input_types=[self.t_dtensor([25], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 25, 1, 1], self.t_f32()), self.t_dtensor([0, 25], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1223 = self.Op("pd_kernel.phi_kernel", 1223, input_types=[self.t_dtensor([-1, 25, 256, 88], self.t_f32()), self.t_dtensor([1, 25, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 25, 256, 88], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1224 = self.Op("pd_kernel.phi_kernel", 1224, input_types=[self.t_dtensor([-1, 25, 256, 88], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"perm":self.a_array(self.a_i32(0), self.a_i32(2), self.a_i32(3), self.a_i32(1)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.transpose"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("transpose"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1225 = self.Op("pd_kernel.phi_kernel", 1225, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1226 = self.Op("pd_kernel.phi_kernel", 1226, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1227 = self.Op("pd_kernel.phi_kernel", 1227, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256, 256, 9, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(4), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1228 = self.Op("pd_kernel.phi_kernel", 1228, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(256), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1229 = self.Op("pd_kernel.phi_kernel", 1229, input_types=[self.t_dtensor([256], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 256, 1, 1], self.t_f32()), self.t_dtensor([0, 256], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1230 = self.Op("pd_kernel.phi_kernel", 1230, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([1, 256, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1231 = self.Op("pd_kernel.phi_kernel", 1231, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([256], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_dtensor([], self.t_f32()), self.t_null()], attrs={"is_inplace":self.a_bool(True), "is_test":self.a_bool(True), "momentum":self.a_f32("0.9"), "data_format":self.a_str("NCHW"), "kernel_key":self.a_kernel(), "epsilon":self.a_f32("1e-05"), "kernel_name":self.a_str("batch_norm"), "persistable":self.a_array(self.a_bool(False), self.a_bool(True), self.a_bool(True), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.batch_norm_"), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False), self.a_bool(False)), "trainable_statistics":self.a_bool(False), "use_global_stats":self.a_bool(True), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1232 = self.Op("pd_kernel.phi_kernel", 1232, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([-1, 256, 88, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1233 = self.Op("pd_kernel.phi_kernel", 1233, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.relu_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("relu"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1234 = self.Op("pd_kernel.phi_kernel", 1234, input_types=[], output_types=[self.t_dtensor([2], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1235 = self.Op("pd_kernel.phi_kernel", 1235, input_types=[self.t_dtensor([-1, 256, 88, 25], self.t_f32()), self.t_dtensor([2], self.t_i64())], output_types=[self.t_dtensor([-1, 256, 1, 1], self.t_f32())], attrs={"ceil_mode":self.a_bool(False), "persistable":self.a_array(self.a_bool(False)), "exclusive":self.a_bool(True), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("pool2d"), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.pool2d"), "strides":self.a_array(self.a_i32(1), self.a_i32(1)), "adaptive":self.a_bool(True), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "pooling_type":self.a_str("avg"), "global_pooling":self.a_bool(False), "data_format":self.a_str("NCHW"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1236 = self.Op("pd_kernel.phi_kernel", 1236, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("1"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1237 = self.Op("pd_kernel.phi_kernel", 1237, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("256"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1238 = self.Op("pd_kernel.phi_kernel", 1238, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("1"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1239 = self.Op("pd_kernel.phi_kernel", 1239, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("1"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1240 = self.Op("builtin.combine", 1240, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1241 = self.Op("pd_kernel.phi_kernel", 1241, input_types=[self.t_dtensor([-1, 256, 1, 1], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, 1, 256, 1, 1], self.t_f32()), self.t_dtensor([0, -1, 256, 1, 1], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1242 = self.Op("pd_kernel.phi_kernel", 1242, input_types=[self.t_dtensor([-1, 1, 256, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 256, 1, 1], self.t_f32())], attrs={"axis":self.a_intarray(1), "keepdim":self.a_bool(False), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.mean"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("mean"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1243 = self.Op("pd_kernel.phi_kernel", 1243, input_types=[self.t_dtensor([-1, 256, 1, 1], self.t_f32()), self.t_dtensor([30, 256, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 30, 1, 1], self.t_f32())], attrs={"strides":self.a_array(self.a_i32(1), self.a_i32(1)), "dilations":self.a_array(self.a_i32(1), self.a_i32(1)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("conv2d"), "groups":self.a_i32(1), "persistable":self.a_array(self.a_bool(False)), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.conv2d"), "data_format":self.a_str("NCHW"), "paddings":self.a_array(self.a_i32(0), self.a_i32(0)), "padding_algorithm":self.a_str("EXPLICIT"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1244 = self.Op("pd_kernel.phi_kernel", 1244, input_types=[], output_types=[self.t_dtensor([4], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1), self.a_i64(30), self.a_i64(1), self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1245 = self.Op("pd_kernel.phi_kernel", 1245, input_types=[self.t_dtensor([30], self.t_f32()), self.t_dtensor([4], self.t_i64())], output_types=[self.t_dtensor([1, 30, 1, 1], self.t_f32()), self.t_dtensor([0, 30], self.t_f32())], attrs={"stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.phi_kernel_1246 = self.Op("pd_kernel.phi_kernel", 1246, input_types=[self.t_dtensor([-1, 30, 1, 1], self.t_f32()), self.t_dtensor([1, 30, 1, 1], self.t_f32())], output_types=[self.t_dtensor([-1, 30, 1, 1], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.add_"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("add"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1247 = self.Op("pd_kernel.phi_kernel", 1247, input_types=[self.t_dtensor([-1, 30, 1, 1], self.t_f32())], output_types=[self.t_dtensor([4], self.t_i32())], attrs={"stop_gradient":self.a_array(self.a_bool(False)), "op_name":self.a_str("pd_op.shape"), "persistable":self.a_array(self.a_bool(False)), "kernel_name":self.a_str("shape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1248 = self.Op("pd_kernel.phi_kernel", 1248, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(0)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1249 = self.Op("pd_kernel.phi_kernel", 1249, input_types=[], output_types=[self.t_dtensor([1], self.t_i64())], attrs={"dtype":self.a_dtype("int64"), "value":self.a_array(self.a_i64(1)), "stop_gradient":self.a_array(self.a_bool(True)), "op_name":self.a_str("pd_op.full_int_array"), "place":self.a_place("cpu"), "kernel_name":self.a_str("full_int_array"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1250 = self.Op("pd_kernel.phi_kernel", 1250, input_types=[self.t_dtensor([4], self.t_i32()), self.t_dtensor([1], self.t_i64()), self.t_dtensor([1], self.t_i64())], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"axes":self.a_array(self.a_i64(0)), "kernel_key":self.a_kernel(), "kernel_name":self.a_str("slice"), "persistable":self.a_array(self.a_bool(False)), "infer_flags":self.a_array(self.a_i64(1)), "decrease_axis":self.a_array(self.a_i64(0)), "op_name":self.a_str("pd_op.slice"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1251 = self.Op("pd_kernel.phi_kernel", 1251, input_types=[], output_types=[self.t_dtensor([1], self.t_i32())], attrs={"value":self.a_f32("-1"), "kernel_key":self.a_kernel(), "dtype":self.a_dtype("int32"), "kernel_name":self.a_str("full"), "persistable":self.a_array(self.a_bool(False)), "place":self.a_place("cpu"), "shape":self.a_intarray(1), "op_name":self.a_str("pd_op.full"), "stop_gradient":self.a_array(self.a_bool(False)), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.combine_1252 = self.Op("builtin.combine", 1252, input_types=[self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32())], output_types=[self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], attrs={"__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()))})

    self.phi_kernel_1253 = self.Op("pd_kernel.phi_kernel", 1253, input_types=[self.t_dtensor([-1, 30, 1, 1], self.t_f32()), self.t_vec(self.t_dtensor([1], self.t_i32()), self.t_dtensor([1], self.t_i32()))], output_types=[self.t_dtensor([-1, -1], self.t_f32()), self.t_dtensor([0, -1, 30, 1, 1], self.t_f32())], attrs={"is_inplace":self.a_bool(True), "stop_gradient":self.a_array(self.a_bool(False), self.a_bool(False)), "op_name":self.a_str("pd_op.reshape_"), "persistable":self.a_array(self.a_bool(False), self.a_bool(False)), "kernel_name":self.a_str("reshape"), "kernel_key":self.a_kernel(), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array(self.a_symbol(self.s_null()), self.a_symbol(self.s_null()))})

    self.shadow_output_1254 = self.Op("builtin.shadow_output", 1254, input_types=[self.t_dtensor([-1, -1], self.t_f32())], output_types=[], attrs={"output_name":self.a_str("reshape2_62.tmp_0"), "__operands_symbols_signature__":self.a_array(self.a_symbol(self.s_null())), "__results_symbols_signature__":self.a_array()})

    self.module_629 = self.Op("builtin.module", 629, input_types=[], output_types=[], attrs={"program":self.a_pointer("0x71476c0"), "__operands_symbols_signature__":self.a_array(), "__results_symbols_signature__":self.a_array()}, block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]], block_positional_arg_types=[[[]]], block_keyword_arg_types=[[[]]], )

    

  def module_629_block00(self, call):

    def ret_lambda_module_629_block00():

      parameter_6300, = call(self.parameter_630)

      parameter_6310, = call(self.parameter_631)

      parameter_6320, = call(self.parameter_632)

      parameter_6330, = call(self.parameter_633)

      parameter_6340, = call(self.parameter_634)

      parameter_6350, = call(self.parameter_635)

      parameter_6360, = call(self.parameter_636)

      parameter_6370, = call(self.parameter_637)

      parameter_6380, = call(self.parameter_638)

      parameter_6390, = call(self.parameter_639)

      parameter_6400, = call(self.parameter_640)

      parameter_6410, = call(self.parameter_641)

      parameter_6420, = call(self.parameter_642)

      parameter_6430, = call(self.parameter_643)

      parameter_6440, = call(self.parameter_644)

      parameter_6450, = call(self.parameter_645)

      parameter_6460, = call(self.parameter_646)

      parameter_6470, = call(self.parameter_647)

      parameter_6480, = call(self.parameter_648)

      parameter_6490, = call(self.parameter_649)

      parameter_6500, = call(self.parameter_650)

      parameter_6510, = call(self.parameter_651)

      parameter_6520, = call(self.parameter_652)

      parameter_6530, = call(self.parameter_653)

      parameter_6540, = call(self.parameter_654)

      parameter_6550, = call(self.parameter_655)

      parameter_6560, = call(self.parameter_656)

      parameter_6570, = call(self.parameter_657)

      parameter_6580, = call(self.parameter_658)

      parameter_6590, = call(self.parameter_659)

      parameter_6600, = call(self.parameter_660)

      parameter_6610, = call(self.parameter_661)

      parameter_6620, = call(self.parameter_662)

      parameter_6630, = call(self.parameter_663)

      parameter_6640, = call(self.parameter_664)

      parameter_6650, = call(self.parameter_665)

      parameter_6660, = call(self.parameter_666)

      parameter_6670, = call(self.parameter_667)

      parameter_6680, = call(self.parameter_668)

      parameter_6690, = call(self.parameter_669)

      parameter_6700, = call(self.parameter_670)

      parameter_6710, = call(self.parameter_671)

      parameter_6720, = call(self.parameter_672)

      parameter_6730, = call(self.parameter_673)

      parameter_6740, = call(self.parameter_674)

      parameter_6750, = call(self.parameter_675)

      parameter_6760, = call(self.parameter_676)

      parameter_6770, = call(self.parameter_677)

      parameter_6780, = call(self.parameter_678)

      parameter_6790, = call(self.parameter_679)

      parameter_6800, = call(self.parameter_680)

      parameter_6810, = call(self.parameter_681)

      parameter_6820, = call(self.parameter_682)

      parameter_6830, = call(self.parameter_683)

      parameter_6840, = call(self.parameter_684)

      parameter_6850, = call(self.parameter_685)

      parameter_6860, = call(self.parameter_686)

      parameter_6870, = call(self.parameter_687)

      parameter_6880, = call(self.parameter_688)

      parameter_6890, = call(self.parameter_689)

      parameter_6900, = call(self.parameter_690)

      parameter_6910, = call(self.parameter_691)

      parameter_6920, = call(self.parameter_692)

      parameter_6930, = call(self.parameter_693)

      parameter_6940, = call(self.parameter_694)

      parameter_6950, = call(self.parameter_695)

      parameter_6960, = call(self.parameter_696)

      parameter_6970, = call(self.parameter_697)

      parameter_6980, = call(self.parameter_698)

      parameter_6990, = call(self.parameter_699)

      parameter_7000, = call(self.parameter_700)

      parameter_7010, = call(self.parameter_701)

      parameter_7020, = call(self.parameter_702)

      parameter_7030, = call(self.parameter_703)

      parameter_7040, = call(self.parameter_704)

      parameter_7050, = call(self.parameter_705)

      parameter_7060, = call(self.parameter_706)

      parameter_7070, = call(self.parameter_707)

      parameter_7080, = call(self.parameter_708)

      parameter_7090, = call(self.parameter_709)

      parameter_7100, = call(self.parameter_710)

      parameter_7110, = call(self.parameter_711)

      parameter_7120, = call(self.parameter_712)

      parameter_7130, = call(self.parameter_713)

      parameter_7140, = call(self.parameter_714)

      parameter_7150, = call(self.parameter_715)

      parameter_7160, = call(self.parameter_716)

      parameter_7170, = call(self.parameter_717)

      parameter_7180, = call(self.parameter_718)

      parameter_7190, = call(self.parameter_719)

      parameter_7200, = call(self.parameter_720)

      parameter_7210, = call(self.parameter_721)

      parameter_7220, = call(self.parameter_722)

      parameter_7230, = call(self.parameter_723)

      parameter_7240, = call(self.parameter_724)

      parameter_7250, = call(self.parameter_725)

      parameter_7260, = call(self.parameter_726)

      parameter_7270, = call(self.parameter_727)

      parameter_7280, = call(self.parameter_728)

      parameter_7290, = call(self.parameter_729)

      parameter_7300, = call(self.parameter_730)

      parameter_7310, = call(self.parameter_731)

      parameter_7320, = call(self.parameter_732)

      parameter_7330, = call(self.parameter_733)

      parameter_7340, = call(self.parameter_734)

      parameter_7350, = call(self.parameter_735)

      parameter_7360, = call(self.parameter_736)

      parameter_7370, = call(self.parameter_737)

      parameter_7380, = call(self.parameter_738)

      parameter_7390, = call(self.parameter_739)

      parameter_7400, = call(self.parameter_740)

      parameter_7410, = call(self.parameter_741)

      parameter_7420, = call(self.parameter_742)

      parameter_7430, = call(self.parameter_743)

      parameter_7440, = call(self.parameter_744)

      parameter_7450, = call(self.parameter_745)

      parameter_7460, = call(self.parameter_746)

      parameter_7470, = call(self.parameter_747)

      parameter_7480, = call(self.parameter_748)

      parameter_7490, = call(self.parameter_749)

      parameter_7500, = call(self.parameter_750)

      parameter_7510, = call(self.parameter_751)

      parameter_7520, = call(self.parameter_752)

      parameter_7530, = call(self.parameter_753)

      parameter_7540, = call(self.parameter_754)

      parameter_7550, = call(self.parameter_755)

      parameter_7560, = call(self.parameter_756)

      parameter_7570, = call(self.parameter_757)

      parameter_7580, = call(self.parameter_758)

      parameter_7590, = call(self.parameter_759)

      parameter_7600, = call(self.parameter_760)

      parameter_7610, = call(self.parameter_761)

      parameter_7620, = call(self.parameter_762)

      parameter_7630, = call(self.parameter_763)

      parameter_7640, = call(self.parameter_764)

      parameter_7650, = call(self.parameter_765)

      parameter_7660, = call(self.parameter_766)

      parameter_7670, = call(self.parameter_767)

      parameter_7680, = call(self.parameter_768)

      parameter_7690, = call(self.parameter_769)

      parameter_7700, = call(self.parameter_770)

      parameter_7710, = call(self.parameter_771)

      parameter_7720, = call(self.parameter_772)

      parameter_7730, = call(self.parameter_773)

      parameter_7740, = call(self.parameter_774)

      parameter_7750, = call(self.parameter_775)

      parameter_7760, = call(self.parameter_776)

      parameter_7770, = call(self.parameter_777)

      parameter_7780, = call(self.parameter_778)

      parameter_7790, = call(self.parameter_779)

      parameter_7800, = call(self.parameter_780)

      parameter_7810, = call(self.parameter_781)

      parameter_7820, = call(self.parameter_782)

      parameter_7830, = call(self.parameter_783)

      parameter_7840, = call(self.parameter_784)

      parameter_7850, = call(self.parameter_785)

      parameter_7860, = call(self.parameter_786)

      parameter_7870, = call(self.parameter_787)

      parameter_7880, = call(self.parameter_788)

      parameter_7890, = call(self.parameter_789)

      parameter_7900, = call(self.parameter_790)

      parameter_7910, = call(self.parameter_791)

      parameter_7920, = call(self.parameter_792)

      parameter_7930, = call(self.parameter_793)

      parameter_7940, = call(self.parameter_794)

      parameter_7950, = call(self.parameter_795)

      parameter_7960, = call(self.parameter_796)

      parameter_7970, = call(self.parameter_797)

      parameter_7980, = call(self.parameter_798)

      parameter_7990, = call(self.parameter_799)

      parameter_8000, = call(self.parameter_800)

      parameter_8010, = call(self.parameter_801)

      parameter_8020, = call(self.parameter_802)

      parameter_8030, = call(self.parameter_803)

      parameter_8040, = call(self.parameter_804)

      parameter_8050, = call(self.parameter_805)

      parameter_8060, = call(self.parameter_806)

      parameter_8070, = call(self.parameter_807)

      parameter_8080, = call(self.parameter_808)

      parameter_8090, = call(self.parameter_809)

      parameter_8100, = call(self.parameter_810)

      parameter_8110, = call(self.parameter_811)

      parameter_8120, = call(self.parameter_812)

      parameter_8130, = call(self.parameter_813)

      parameter_8140, = call(self.parameter_814)

      parameter_8150, = call(self.parameter_815)

      parameter_8160, = call(self.parameter_816)

      parameter_8170, = call(self.parameter_817)

      parameter_8180, = call(self.parameter_818)

      parameter_8190, = call(self.parameter_819)

      parameter_8200, = call(self.parameter_820)

      parameter_8210, = call(self.parameter_821)

      parameter_8220, = call(self.parameter_822)

      parameter_8230, = call(self.parameter_823)

      parameter_8240, = call(self.parameter_824)

      parameter_8250, = call(self.parameter_825)

      phi_kernel_8260, = call(self.phi_kernel_826)

      phi_kernel_8280, = call(self.phi_kernel_828, phi_kernel_8260)

      phi_kernel_8290, = call(self.phi_kernel_829)

      phi_kernel_8300, = call(self.phi_kernel_830)

      phi_kernel_8310, = call(self.phi_kernel_831, phi_kernel_8280, phi_kernel_8290, phi_kernel_8300)

      phi_kernel_8320, = call(self.phi_kernel_832, phi_kernel_8260)

      phi_kernel_8330, = call(self.phi_kernel_833)

      phi_kernel_8340, = call(self.phi_kernel_834, phi_kernel_8310, phi_kernel_8330)

      phi_kernel_8350, = call(self.phi_kernel_835)

      phi_kernel_8360, = call(self.phi_kernel_836)

      phi_kernel_8370, = call(self.phi_kernel_837)

      combine_8380, = call(self.combine_838, phi_kernel_8340, phi_kernel_8350, phi_kernel_8360, phi_kernel_8370)

      phi_kernel_8390, phi_kernel_8391, = call(self.phi_kernel_839, phi_kernel_8320, combine_8380)

      phi_kernel_8400, = call(self.phi_kernel_840, phi_kernel_8390, parameter_6300)

      phi_kernel_8410, = call(self.phi_kernel_841)

      phi_kernel_8420, phi_kernel_8421, = call(self.phi_kernel_842, parameter_6310, phi_kernel_8410)

      phi_kernel_8430, = call(self.phi_kernel_843, phi_kernel_8400, phi_kernel_8420)

      phi_kernel_8440, = call(self.phi_kernel_844, phi_kernel_8430)

      phi_kernel_8450, = call(self.phi_kernel_845)

      phi_kernel_8460, = call(self.phi_kernel_846)

      phi_kernel_8470, = call(self.phi_kernel_847, phi_kernel_8440, phi_kernel_8450, phi_kernel_8460)

      phi_kernel_8480, = call(self.phi_kernel_848)

      phi_kernel_8490, = call(self.phi_kernel_849)

      phi_kernel_8500, = call(self.phi_kernel_850)

      phi_kernel_8510, = call(self.phi_kernel_851)

      combine_8520, = call(self.combine_852, phi_kernel_8470, phi_kernel_8480, phi_kernel_8490, phi_kernel_8500, phi_kernel_8510)

      phi_kernel_8530, phi_kernel_8531, = call(self.phi_kernel_853, phi_kernel_8430, combine_8520)

      phi_kernel_8540, = call(self.phi_kernel_854, phi_kernel_8530)

      phi_kernel_8550, = call(self.phi_kernel_855)

      phi_kernel_8560, = call(self.phi_kernel_856)

      phi_kernel_8570, = call(self.phi_kernel_857)

      combine_8580, = call(self.combine_858, phi_kernel_8470, phi_kernel_8550, phi_kernel_8560, phi_kernel_8570)

      phi_kernel_8590, phi_kernel_8591, = call(self.phi_kernel_859, phi_kernel_8540, combine_8580)

      phi_kernel_8600, = call(self.phi_kernel_860, phi_kernel_8590)

      phi_kernel_8610, = call(self.phi_kernel_861, phi_kernel_8600, parameter_6320)

      phi_kernel_8620, = call(self.phi_kernel_862)

      phi_kernel_8630, phi_kernel_8631, = call(self.phi_kernel_863, parameter_6330, phi_kernel_8620)

      phi_kernel_8640, = call(self.phi_kernel_864, phi_kernel_8610, phi_kernel_8630)

      phi_kernel_8650, = call(self.phi_kernel_865, phi_kernel_8640)

      phi_kernel_8660, phi_kernel_8661, phi_kernel_8662, phi_kernel_8663, phi_kernel_8664, phi_kernel_8665, = call(self.phi_kernel_866, phi_kernel_8650, parameter_6350, parameter_6370, parameter_6360, parameter_6340)

      phi_kernel_8670, = call(self.phi_kernel_867, phi_kernel_8660)

      phi_kernel_8680, = call(self.phi_kernel_868, phi_kernel_8670, parameter_6380)

      phi_kernel_8690, = call(self.phi_kernel_869)

      phi_kernel_8700, phi_kernel_8701, = call(self.phi_kernel_870, parameter_6390, phi_kernel_8690)

      phi_kernel_8710, = call(self.phi_kernel_871, phi_kernel_8680, phi_kernel_8700)

      phi_kernel_8720, phi_kernel_8721, phi_kernel_8722, phi_kernel_8723, phi_kernel_8724, phi_kernel_8725, = call(self.phi_kernel_872, phi_kernel_8710, parameter_6410, parameter_6430, parameter_6420, parameter_6400)

      phi_kernel_8730, = call(self.phi_kernel_873, phi_kernel_8720)

      phi_kernel_8740, = call(self.phi_kernel_874, phi_kernel_8730, parameter_6440)

      phi_kernel_8750, = call(self.phi_kernel_875)

      phi_kernel_8760, phi_kernel_8761, = call(self.phi_kernel_876, parameter_6450, phi_kernel_8750)

      phi_kernel_8770, = call(self.phi_kernel_877, phi_kernel_8740, phi_kernel_8760)

      phi_kernel_8780, phi_kernel_8781, phi_kernel_8782, phi_kernel_8783, phi_kernel_8784, phi_kernel_8785, = call(self.phi_kernel_878, phi_kernel_8770, parameter_6470, parameter_6490, parameter_6480, parameter_6460)

      phi_kernel_8790, = call(self.phi_kernel_879, phi_kernel_8730, parameter_6500)

      phi_kernel_8800, = call(self.phi_kernel_880)

      phi_kernel_8810, phi_kernel_8811, = call(self.phi_kernel_881, parameter_6510, phi_kernel_8800)

      phi_kernel_8820, = call(self.phi_kernel_882, phi_kernel_8790, phi_kernel_8810)

      phi_kernel_8830, = call(self.phi_kernel_883, phi_kernel_8820)

      phi_kernel_8840, = call(self.phi_kernel_884)

      phi_kernel_8850, = call(self.phi_kernel_885)

      phi_kernel_8860, = call(self.phi_kernel_886, phi_kernel_8830, phi_kernel_8840, phi_kernel_8850)

      phi_kernel_8870, = call(self.phi_kernel_887)

      phi_kernel_8880, = call(self.phi_kernel_888)

      phi_kernel_8890, = call(self.phi_kernel_889)

      phi_kernel_8900, = call(self.phi_kernel_890)

      combine_8910, = call(self.combine_891, phi_kernel_8860, phi_kernel_8870, phi_kernel_8880, phi_kernel_8890, phi_kernel_8900)

      phi_kernel_8920, phi_kernel_8921, = call(self.phi_kernel_892, phi_kernel_8820, combine_8910)

      phi_kernel_8930, = call(self.phi_kernel_893, phi_kernel_8920)

      phi_kernel_8940, = call(self.phi_kernel_894)

      phi_kernel_8950, = call(self.phi_kernel_895)

      phi_kernel_8960, = call(self.phi_kernel_896)

      combine_8970, = call(self.combine_897, phi_kernel_8860, phi_kernel_8940, phi_kernel_8950, phi_kernel_8960)

      phi_kernel_8980, phi_kernel_8981, = call(self.phi_kernel_898, phi_kernel_8930, combine_8970)

      phi_kernel_8990, = call(self.phi_kernel_899, phi_kernel_8980)

      phi_kernel_9000, = call(self.phi_kernel_900, phi_kernel_8990, parameter_6520)

      phi_kernel_9010, = call(self.phi_kernel_901)

      phi_kernel_9020, phi_kernel_9021, = call(self.phi_kernel_902, parameter_6530, phi_kernel_9010)

      phi_kernel_9030, = call(self.phi_kernel_903, phi_kernel_9000, phi_kernel_9020)

      phi_kernel_9040, = call(self.phi_kernel_904, phi_kernel_9030)

      phi_kernel_9050, phi_kernel_9051, phi_kernel_9052, phi_kernel_9053, phi_kernel_9054, phi_kernel_9055, = call(self.phi_kernel_905, phi_kernel_9040, parameter_6550, parameter_6570, parameter_6560, parameter_6540)

      phi_kernel_9060, = call(self.phi_kernel_906, phi_kernel_9050)

      phi_kernel_9070, = call(self.phi_kernel_907, phi_kernel_9060, parameter_6580)

      phi_kernel_9080, = call(self.phi_kernel_908)

      phi_kernel_9090, phi_kernel_9091, = call(self.phi_kernel_909, parameter_6590, phi_kernel_9080)

      phi_kernel_9100, = call(self.phi_kernel_910, phi_kernel_9070, phi_kernel_9090)

      phi_kernel_9110, phi_kernel_9111, phi_kernel_9112, phi_kernel_9113, phi_kernel_9114, phi_kernel_9115, = call(self.phi_kernel_911, phi_kernel_9100, parameter_6610, parameter_6630, parameter_6620, parameter_6600)

      phi_kernel_9120, = call(self.phi_kernel_912, phi_kernel_9110, phi_kernel_8780)

      phi_kernel_9130, = call(self.phi_kernel_913, phi_kernel_9120)

      phi_kernel_9140, = call(self.phi_kernel_914, phi_kernel_9130, parameter_6640)

      phi_kernel_9150, = call(self.phi_kernel_915)

      phi_kernel_9160, phi_kernel_9161, = call(self.phi_kernel_916, parameter_6650, phi_kernel_9150)

      phi_kernel_9170, = call(self.phi_kernel_917, phi_kernel_9140, phi_kernel_9160)

      phi_kernel_9180, phi_kernel_9181, phi_kernel_9182, phi_kernel_9183, phi_kernel_9184, phi_kernel_9185, = call(self.phi_kernel_918, phi_kernel_9170, parameter_6670, parameter_6690, parameter_6680, parameter_6660)

      phi_kernel_9190, = call(self.phi_kernel_919, phi_kernel_9130, parameter_6700)

      phi_kernel_9200, = call(self.phi_kernel_920)

      phi_kernel_9210, phi_kernel_9211, = call(self.phi_kernel_921, parameter_6710, phi_kernel_9200)

      phi_kernel_9220, = call(self.phi_kernel_922, phi_kernel_9190, phi_kernel_9210)

      phi_kernel_9230, = call(self.phi_kernel_923, phi_kernel_9220)

      phi_kernel_9240, = call(self.phi_kernel_924)

      phi_kernel_9250, = call(self.phi_kernel_925)

      phi_kernel_9260, = call(self.phi_kernel_926, phi_kernel_9230, phi_kernel_9240, phi_kernel_9250)

      phi_kernel_9270, = call(self.phi_kernel_927)

      phi_kernel_9280, = call(self.phi_kernel_928)

      phi_kernel_9290, = call(self.phi_kernel_929)

      phi_kernel_9300, = call(self.phi_kernel_930)

      combine_9310, = call(self.combine_931, phi_kernel_9260, phi_kernel_9270, phi_kernel_9280, phi_kernel_9290, phi_kernel_9300)

      phi_kernel_9320, phi_kernel_9321, = call(self.phi_kernel_932, phi_kernel_9220, combine_9310)

      phi_kernel_9330, = call(self.phi_kernel_933, phi_kernel_9320)

      phi_kernel_9340, = call(self.phi_kernel_934)

      phi_kernel_9350, = call(self.phi_kernel_935)

      phi_kernel_9360, = call(self.phi_kernel_936)

      combine_9370, = call(self.combine_937, phi_kernel_9260, phi_kernel_9340, phi_kernel_9350, phi_kernel_9360)

      phi_kernel_9380, phi_kernel_9381, = call(self.phi_kernel_938, phi_kernel_9330, combine_9370)

      phi_kernel_9390, = call(self.phi_kernel_939, phi_kernel_9380)

      phi_kernel_9400, = call(self.phi_kernel_940, phi_kernel_9390, parameter_6720)

      phi_kernel_9410, = call(self.phi_kernel_941)

      phi_kernel_9420, phi_kernel_9421, = call(self.phi_kernel_942, parameter_6730, phi_kernel_9410)

      phi_kernel_9430, = call(self.phi_kernel_943, phi_kernel_9400, phi_kernel_9420)

      phi_kernel_9440, = call(self.phi_kernel_944, phi_kernel_9430)

      phi_kernel_9450, phi_kernel_9451, phi_kernel_9452, phi_kernel_9453, phi_kernel_9454, phi_kernel_9455, = call(self.phi_kernel_945, phi_kernel_9440, parameter_6750, parameter_6770, parameter_6760, parameter_6740)

      phi_kernel_9460, = call(self.phi_kernel_946, phi_kernel_9450)

      phi_kernel_9470, = call(self.phi_kernel_947, phi_kernel_9460, parameter_6780)

      phi_kernel_9480, = call(self.phi_kernel_948)

      phi_kernel_9490, phi_kernel_9491, = call(self.phi_kernel_949, parameter_6790, phi_kernel_9480)

      phi_kernel_9500, = call(self.phi_kernel_950, phi_kernel_9470, phi_kernel_9490)

      phi_kernel_9510, phi_kernel_9511, phi_kernel_9512, phi_kernel_9513, phi_kernel_9514, phi_kernel_9515, = call(self.phi_kernel_951, phi_kernel_9500, parameter_6810, parameter_6830, parameter_6820, parameter_6800)

      phi_kernel_9520, = call(self.phi_kernel_952, phi_kernel_9510, phi_kernel_9180)

      phi_kernel_9530, = call(self.phi_kernel_953, phi_kernel_9520)

      phi_kernel_9540, = call(self.phi_kernel_954, phi_kernel_9530, parameter_6840)

      phi_kernel_9550, = call(self.phi_kernel_955)

      phi_kernel_9560, phi_kernel_9561, = call(self.phi_kernel_956, parameter_6850, phi_kernel_9550)

      phi_kernel_9570, = call(self.phi_kernel_957, phi_kernel_9540, phi_kernel_9560)

      phi_kernel_9580, phi_kernel_9581, phi_kernel_9582, phi_kernel_9583, phi_kernel_9584, phi_kernel_9585, = call(self.phi_kernel_958, phi_kernel_9570, parameter_6870, parameter_6890, parameter_6880, parameter_6860)

      phi_kernel_9590, = call(self.phi_kernel_959, phi_kernel_9530, parameter_6900)

      phi_kernel_9600, = call(self.phi_kernel_960)

      phi_kernel_9610, phi_kernel_9611, = call(self.phi_kernel_961, parameter_6910, phi_kernel_9600)

      phi_kernel_9620, = call(self.phi_kernel_962, phi_kernel_9590, phi_kernel_9610)

      phi_kernel_9630, = call(self.phi_kernel_963, phi_kernel_9620)

      phi_kernel_9640, = call(self.phi_kernel_964)

      phi_kernel_9650, = call(self.phi_kernel_965)

      phi_kernel_9660, = call(self.phi_kernel_966, phi_kernel_9630, phi_kernel_9640, phi_kernel_9650)

      phi_kernel_9670, = call(self.phi_kernel_967)

      phi_kernel_9680, = call(self.phi_kernel_968)

      phi_kernel_9690, = call(self.phi_kernel_969)

      phi_kernel_9700, = call(self.phi_kernel_970)

      combine_9710, = call(self.combine_971, phi_kernel_9660, phi_kernel_9670, phi_kernel_9680, phi_kernel_9690, phi_kernel_9700)

      phi_kernel_9720, phi_kernel_9721, = call(self.phi_kernel_972, phi_kernel_9620, combine_9710)

      phi_kernel_9730, = call(self.phi_kernel_973, phi_kernel_9720)

      phi_kernel_9740, = call(self.phi_kernel_974)

      phi_kernel_9750, = call(self.phi_kernel_975)

      phi_kernel_9760, = call(self.phi_kernel_976)

      combine_9770, = call(self.combine_977, phi_kernel_9660, phi_kernel_9740, phi_kernel_9750, phi_kernel_9760)

      phi_kernel_9780, phi_kernel_9781, = call(self.phi_kernel_978, phi_kernel_9730, combine_9770)

      phi_kernel_9790, = call(self.phi_kernel_979, phi_kernel_9780)

      phi_kernel_9800, = call(self.phi_kernel_980, phi_kernel_9790, parameter_6920)

      phi_kernel_9810, = call(self.phi_kernel_981)

      phi_kernel_9820, phi_kernel_9821, = call(self.phi_kernel_982, parameter_6930, phi_kernel_9810)

      phi_kernel_9830, = call(self.phi_kernel_983, phi_kernel_9800, phi_kernel_9820)

      phi_kernel_9840, = call(self.phi_kernel_984, phi_kernel_9830)

      phi_kernel_9850, phi_kernel_9851, phi_kernel_9852, phi_kernel_9853, phi_kernel_9854, phi_kernel_9855, = call(self.phi_kernel_985, phi_kernel_9840, parameter_6950, parameter_6970, parameter_6960, parameter_6940)

      phi_kernel_9860, = call(self.phi_kernel_986, phi_kernel_9850)

      phi_kernel_9870, = call(self.phi_kernel_987, phi_kernel_9860, parameter_6980)

      phi_kernel_9880, = call(self.phi_kernel_988)

      phi_kernel_9890, phi_kernel_9891, = call(self.phi_kernel_989, parameter_6990, phi_kernel_9880)

      phi_kernel_9900, = call(self.phi_kernel_990, phi_kernel_9870, phi_kernel_9890)

      phi_kernel_9910, phi_kernel_9911, phi_kernel_9912, phi_kernel_9913, phi_kernel_9914, phi_kernel_9915, = call(self.phi_kernel_991, phi_kernel_9900, parameter_7010, parameter_7030, parameter_7020, parameter_7000)

      phi_kernel_9920, = call(self.phi_kernel_992, phi_kernel_9910, phi_kernel_9580)

      phi_kernel_9930, = call(self.phi_kernel_993, phi_kernel_9920)

      phi_kernel_9940, = call(self.phi_kernel_994, phi_kernel_9930, parameter_7040)

      phi_kernel_9950, = call(self.phi_kernel_995)

      phi_kernel_9960, phi_kernel_9961, = call(self.phi_kernel_996, parameter_7050, phi_kernel_9950)

      phi_kernel_9970, = call(self.phi_kernel_997, phi_kernel_9940, phi_kernel_9960)

      phi_kernel_9980, phi_kernel_9981, phi_kernel_9982, phi_kernel_9983, phi_kernel_9984, phi_kernel_9985, = call(self.phi_kernel_998, phi_kernel_9970, parameter_7070, parameter_7090, parameter_7080, parameter_7060)

      phi_kernel_9990, = call(self.phi_kernel_999, phi_kernel_9930, parameter_7100)

      phi_kernel_10000, = call(self.phi_kernel_1000)

      phi_kernel_10010, phi_kernel_10011, = call(self.phi_kernel_1001, parameter_7110, phi_kernel_10000)

      phi_kernel_10020, = call(self.phi_kernel_1002, phi_kernel_9990, phi_kernel_10010)

      phi_kernel_10030, = call(self.phi_kernel_1003, phi_kernel_10020)

      phi_kernel_10040, = call(self.phi_kernel_1004)

      phi_kernel_10050, = call(self.phi_kernel_1005)

      phi_kernel_10060, = call(self.phi_kernel_1006, phi_kernel_10030, phi_kernel_10040, phi_kernel_10050)

      phi_kernel_10070, = call(self.phi_kernel_1007)

      phi_kernel_10080, = call(self.phi_kernel_1008)

      phi_kernel_10090, = call(self.phi_kernel_1009)

      phi_kernel_10100, = call(self.phi_kernel_1010)

      combine_10110, = call(self.combine_1011, phi_kernel_10060, phi_kernel_10070, phi_kernel_10080, phi_kernel_10090, phi_kernel_10100)

      phi_kernel_10120, phi_kernel_10121, = call(self.phi_kernel_1012, phi_kernel_10020, combine_10110)

      phi_kernel_10130, = call(self.phi_kernel_1013, phi_kernel_10120)

      phi_kernel_10140, = call(self.phi_kernel_1014)

      phi_kernel_10150, = call(self.phi_kernel_1015)

      phi_kernel_10160, = call(self.phi_kernel_1016)

      combine_10170, = call(self.combine_1017, phi_kernel_10060, phi_kernel_10140, phi_kernel_10150, phi_kernel_10160)

      phi_kernel_10180, phi_kernel_10181, = call(self.phi_kernel_1018, phi_kernel_10130, combine_10170)

      phi_kernel_10190, = call(self.phi_kernel_1019, phi_kernel_10180)

      phi_kernel_10200, = call(self.phi_kernel_1020, phi_kernel_10190, parameter_7120)

      phi_kernel_10210, = call(self.phi_kernel_1021)

      phi_kernel_10220, phi_kernel_10221, = call(self.phi_kernel_1022, parameter_7130, phi_kernel_10210)

      phi_kernel_10230, = call(self.phi_kernel_1023, phi_kernel_10200, phi_kernel_10220)

      phi_kernel_10240, = call(self.phi_kernel_1024, phi_kernel_10230)

      phi_kernel_10250, phi_kernel_10251, phi_kernel_10252, phi_kernel_10253, phi_kernel_10254, phi_kernel_10255, = call(self.phi_kernel_1025, phi_kernel_10240, parameter_7150, parameter_7170, parameter_7160, parameter_7140)

      phi_kernel_10260, = call(self.phi_kernel_1026, phi_kernel_10250)

      phi_kernel_10270, = call(self.phi_kernel_1027, phi_kernel_10260, parameter_7180)

      phi_kernel_10280, = call(self.phi_kernel_1028)

      phi_kernel_10290, phi_kernel_10291, = call(self.phi_kernel_1029, parameter_7190, phi_kernel_10280)

      phi_kernel_10300, = call(self.phi_kernel_1030, phi_kernel_10270, phi_kernel_10290)

      phi_kernel_10310, phi_kernel_10311, phi_kernel_10312, phi_kernel_10313, phi_kernel_10314, phi_kernel_10315, = call(self.phi_kernel_1031, phi_kernel_10300, parameter_7210, parameter_7230, parameter_7220, parameter_7200)

      phi_kernel_10320, = call(self.phi_kernel_1032, phi_kernel_10310, phi_kernel_9980)

      phi_kernel_10330, = call(self.phi_kernel_1033, phi_kernel_10320)

      phi_kernel_10340, = call(self.phi_kernel_1034, phi_kernel_10330, parameter_7240)

      phi_kernel_10350, = call(self.phi_kernel_1035)

      phi_kernel_10360, phi_kernel_10361, = call(self.phi_kernel_1036, parameter_7250, phi_kernel_10350)

      phi_kernel_10370, = call(self.phi_kernel_1037, phi_kernel_10340, phi_kernel_10360)

      phi_kernel_10380, phi_kernel_10381, phi_kernel_10382, phi_kernel_10383, phi_kernel_10384, phi_kernel_10385, = call(self.phi_kernel_1038, phi_kernel_10370, parameter_7270, parameter_7290, parameter_7280, parameter_7260)

      phi_kernel_10390, = call(self.phi_kernel_1039, phi_kernel_10330, parameter_7300)

      phi_kernel_10400, = call(self.phi_kernel_1040)

      phi_kernel_10410, phi_kernel_10411, = call(self.phi_kernel_1041, parameter_7310, phi_kernel_10400)

      phi_kernel_10420, = call(self.phi_kernel_1042, phi_kernel_10390, phi_kernel_10410)

      phi_kernel_10430, = call(self.phi_kernel_1043, phi_kernel_10420)

      phi_kernel_10440, = call(self.phi_kernel_1044)

      phi_kernel_10450, = call(self.phi_kernel_1045)

      phi_kernel_10460, = call(self.phi_kernel_1046, phi_kernel_10430, phi_kernel_10440, phi_kernel_10450)

      phi_kernel_10470, = call(self.phi_kernel_1047)

      phi_kernel_10480, = call(self.phi_kernel_1048)

      phi_kernel_10490, = call(self.phi_kernel_1049)

      phi_kernel_10500, = call(self.phi_kernel_1050)

      combine_10510, = call(self.combine_1051, phi_kernel_10460, phi_kernel_10470, phi_kernel_10480, phi_kernel_10490, phi_kernel_10500)

      phi_kernel_10520, phi_kernel_10521, = call(self.phi_kernel_1052, phi_kernel_10420, combine_10510)

      phi_kernel_10530, = call(self.phi_kernel_1053, phi_kernel_10520)

      phi_kernel_10540, = call(self.phi_kernel_1054)

      phi_kernel_10550, = call(self.phi_kernel_1055)

      phi_kernel_10560, = call(self.phi_kernel_1056)

      combine_10570, = call(self.combine_1057, phi_kernel_10460, phi_kernel_10540, phi_kernel_10550, phi_kernel_10560)

      phi_kernel_10580, phi_kernel_10581, = call(self.phi_kernel_1058, phi_kernel_10530, combine_10570)

      phi_kernel_10590, = call(self.phi_kernel_1059, phi_kernel_10580)

      phi_kernel_10600, = call(self.phi_kernel_1060, phi_kernel_10590, parameter_7320)

      phi_kernel_10610, = call(self.phi_kernel_1061)

      phi_kernel_10620, phi_kernel_10621, = call(self.phi_kernel_1062, parameter_7330, phi_kernel_10610)

      phi_kernel_10630, = call(self.phi_kernel_1063, phi_kernel_10600, phi_kernel_10620)

      phi_kernel_10640, = call(self.phi_kernel_1064, phi_kernel_10630)

      phi_kernel_10650, phi_kernel_10651, phi_kernel_10652, phi_kernel_10653, phi_kernel_10654, phi_kernel_10655, = call(self.phi_kernel_1065, phi_kernel_10640, parameter_7350, parameter_7370, parameter_7360, parameter_7340)

      phi_kernel_10660, = call(self.phi_kernel_1066, phi_kernel_10650)

      phi_kernel_10670, = call(self.phi_kernel_1067, phi_kernel_10660, parameter_7380)

      phi_kernel_10680, = call(self.phi_kernel_1068)

      phi_kernel_10690, phi_kernel_10691, = call(self.phi_kernel_1069, parameter_7390, phi_kernel_10680)

      phi_kernel_10700, = call(self.phi_kernel_1070, phi_kernel_10670, phi_kernel_10690)

      phi_kernel_10710, phi_kernel_10711, phi_kernel_10712, phi_kernel_10713, phi_kernel_10714, phi_kernel_10715, = call(self.phi_kernel_1071, phi_kernel_10700, parameter_7410, parameter_7430, parameter_7420, parameter_7400)

      phi_kernel_10720, = call(self.phi_kernel_1072, phi_kernel_10710, phi_kernel_10380)

      phi_kernel_10730, = call(self.phi_kernel_1073, phi_kernel_10720)

      phi_kernel_10740, = call(self.phi_kernel_1074, phi_kernel_10730, parameter_7440)

      phi_kernel_10750, = call(self.phi_kernel_1075)

      phi_kernel_10760, phi_kernel_10761, = call(self.phi_kernel_1076, parameter_7450, phi_kernel_10750)

      phi_kernel_10770, = call(self.phi_kernel_1077, phi_kernel_10740, phi_kernel_10760)

      phi_kernel_10780, phi_kernel_10781, phi_kernel_10782, phi_kernel_10783, phi_kernel_10784, phi_kernel_10785, = call(self.phi_kernel_1078, phi_kernel_10770, parameter_7470, parameter_7490, parameter_7480, parameter_7460)

      phi_kernel_10790, = call(self.phi_kernel_1079, phi_kernel_10730, parameter_7500)

      phi_kernel_10800, = call(self.phi_kernel_1080)

      phi_kernel_10810, phi_kernel_10811, = call(self.phi_kernel_1081, parameter_7510, phi_kernel_10800)

      phi_kernel_10820, = call(self.phi_kernel_1082, phi_kernel_10790, phi_kernel_10810)

      phi_kernel_10830, = call(self.phi_kernel_1083, phi_kernel_10820)

      phi_kernel_10840, = call(self.phi_kernel_1084)

      phi_kernel_10850, = call(self.phi_kernel_1085)

      phi_kernel_10860, = call(self.phi_kernel_1086, phi_kernel_10830, phi_kernel_10840, phi_kernel_10850)

      phi_kernel_10870, = call(self.phi_kernel_1087)

      phi_kernel_10880, = call(self.phi_kernel_1088)

      phi_kernel_10890, = call(self.phi_kernel_1089)

      phi_kernel_10900, = call(self.phi_kernel_1090)

      combine_10910, = call(self.combine_1091, phi_kernel_10860, phi_kernel_10870, phi_kernel_10880, phi_kernel_10890, phi_kernel_10900)

      phi_kernel_10920, phi_kernel_10921, = call(self.phi_kernel_1092, phi_kernel_10820, combine_10910)

      phi_kernel_10930, = call(self.phi_kernel_1093, phi_kernel_10920)

      phi_kernel_10940, = call(self.phi_kernel_1094)

      phi_kernel_10950, = call(self.phi_kernel_1095)

      phi_kernel_10960, = call(self.phi_kernel_1096)

      combine_10970, = call(self.combine_1097, phi_kernel_10860, phi_kernel_10940, phi_kernel_10950, phi_kernel_10960)

      phi_kernel_10980, phi_kernel_10981, = call(self.phi_kernel_1098, phi_kernel_10930, combine_10970)

      phi_kernel_10990, = call(self.phi_kernel_1099, phi_kernel_10980)

      phi_kernel_11000, = call(self.phi_kernel_1100, phi_kernel_10990, parameter_7520)

      phi_kernel_11010, = call(self.phi_kernel_1101)

      phi_kernel_11020, phi_kernel_11021, = call(self.phi_kernel_1102, parameter_7530, phi_kernel_11010)

      phi_kernel_11030, = call(self.phi_kernel_1103, phi_kernel_11000, phi_kernel_11020)

      phi_kernel_11040, = call(self.phi_kernel_1104, phi_kernel_11030)

      phi_kernel_11050, phi_kernel_11051, phi_kernel_11052, phi_kernel_11053, phi_kernel_11054, phi_kernel_11055, = call(self.phi_kernel_1105, phi_kernel_11040, parameter_7550, parameter_7570, parameter_7560, parameter_7540)

      phi_kernel_11060, = call(self.phi_kernel_1106, phi_kernel_11050)

      phi_kernel_11070, = call(self.phi_kernel_1107, phi_kernel_11060, parameter_7580)

      phi_kernel_11080, = call(self.phi_kernel_1108)

      phi_kernel_11090, phi_kernel_11091, = call(self.phi_kernel_1109, parameter_7590, phi_kernel_11080)

      phi_kernel_11100, = call(self.phi_kernel_1110, phi_kernel_11070, phi_kernel_11090)

      phi_kernel_11110, phi_kernel_11111, phi_kernel_11112, phi_kernel_11113, phi_kernel_11114, phi_kernel_11115, = call(self.phi_kernel_1111, phi_kernel_11100, parameter_7610, parameter_7630, parameter_7620, parameter_7600)

      phi_kernel_11120, = call(self.phi_kernel_1112, phi_kernel_11110, phi_kernel_10780)

      phi_kernel_11130, = call(self.phi_kernel_1113, phi_kernel_11120)

      phi_kernel_11140, = call(self.phi_kernel_1114, phi_kernel_11130, parameter_7640)

      phi_kernel_11150, = call(self.phi_kernel_1115)

      phi_kernel_11160, phi_kernel_11161, = call(self.phi_kernel_1116, parameter_7650, phi_kernel_11150)

      phi_kernel_11170, = call(self.phi_kernel_1117, phi_kernel_11140, phi_kernel_11160)

      phi_kernel_11180, phi_kernel_11181, phi_kernel_11182, phi_kernel_11183, phi_kernel_11184, phi_kernel_11185, = call(self.phi_kernel_1118, phi_kernel_11170, parameter_7670, parameter_7690, parameter_7680, parameter_7660)

      phi_kernel_11190, = call(self.phi_kernel_1119, phi_kernel_11130, parameter_7700)

      phi_kernel_11200, = call(self.phi_kernel_1120)

      phi_kernel_11210, phi_kernel_11211, = call(self.phi_kernel_1121, parameter_7710, phi_kernel_11200)

      phi_kernel_11220, = call(self.phi_kernel_1122, phi_kernel_11190, phi_kernel_11210)

      phi_kernel_11230, = call(self.phi_kernel_1123, phi_kernel_11220)

      phi_kernel_11240, = call(self.phi_kernel_1124)

      phi_kernel_11250, = call(self.phi_kernel_1125)

      phi_kernel_11260, = call(self.phi_kernel_1126, phi_kernel_11230, phi_kernel_11240, phi_kernel_11250)

      phi_kernel_11270, = call(self.phi_kernel_1127)

      phi_kernel_11280, = call(self.phi_kernel_1128)

      phi_kernel_11290, = call(self.phi_kernel_1129)

      phi_kernel_11300, = call(self.phi_kernel_1130)

      combine_11310, = call(self.combine_1131, phi_kernel_11260, phi_kernel_11270, phi_kernel_11280, phi_kernel_11290, phi_kernel_11300)

      phi_kernel_11320, phi_kernel_11321, = call(self.phi_kernel_1132, phi_kernel_11220, combine_11310)

      phi_kernel_11330, = call(self.phi_kernel_1133, phi_kernel_11320)

      phi_kernel_11340, = call(self.phi_kernel_1134)

      phi_kernel_11350, = call(self.phi_kernel_1135)

      phi_kernel_11360, = call(self.phi_kernel_1136)

      combine_11370, = call(self.combine_1137, phi_kernel_11260, phi_kernel_11340, phi_kernel_11350, phi_kernel_11360)

      phi_kernel_11380, phi_kernel_11381, = call(self.phi_kernel_1138, phi_kernel_11330, combine_11370)

      phi_kernel_11390, = call(self.phi_kernel_1139, phi_kernel_11380)

      phi_kernel_11400, = call(self.phi_kernel_1140, phi_kernel_11390, parameter_7720)

      phi_kernel_11410, = call(self.phi_kernel_1141)

      phi_kernel_11420, phi_kernel_11421, = call(self.phi_kernel_1142, parameter_7730, phi_kernel_11410)

      phi_kernel_11430, = call(self.phi_kernel_1143, phi_kernel_11400, phi_kernel_11420)

      phi_kernel_11440, = call(self.phi_kernel_1144, phi_kernel_11430)

      phi_kernel_11450, phi_kernel_11451, phi_kernel_11452, phi_kernel_11453, phi_kernel_11454, phi_kernel_11455, = call(self.phi_kernel_1145, phi_kernel_11440, parameter_7750, parameter_7770, parameter_7760, parameter_7740)

      phi_kernel_11460, = call(self.phi_kernel_1146, phi_kernel_11450)

      phi_kernel_11470, = call(self.phi_kernel_1147, phi_kernel_11460, parameter_7780)

      phi_kernel_11480, = call(self.phi_kernel_1148)

      phi_kernel_11490, phi_kernel_11491, = call(self.phi_kernel_1149, parameter_7790, phi_kernel_11480)

      phi_kernel_11500, = call(self.phi_kernel_1150, phi_kernel_11470, phi_kernel_11490)

      phi_kernel_11510, phi_kernel_11511, phi_kernel_11512, phi_kernel_11513, phi_kernel_11514, phi_kernel_11515, = call(self.phi_kernel_1151, phi_kernel_11500, parameter_7810, parameter_7830, parameter_7820, parameter_7800)

      phi_kernel_11520, = call(self.phi_kernel_1152, phi_kernel_11510, phi_kernel_11180)

      phi_kernel_11530, = call(self.phi_kernel_1153, phi_kernel_11520)

      phi_kernel_11540, = call(self.phi_kernel_1154, phi_kernel_11530, parameter_7840)

      phi_kernel_11550, = call(self.phi_kernel_1155)

      phi_kernel_11560, phi_kernel_11561, = call(self.phi_kernel_1156, parameter_7850, phi_kernel_11550)

      phi_kernel_11570, = call(self.phi_kernel_1157, phi_kernel_11540, phi_kernel_11560)

      phi_kernel_11580, phi_kernel_11581, phi_kernel_11582, phi_kernel_11583, phi_kernel_11584, phi_kernel_11585, = call(self.phi_kernel_1158, phi_kernel_11570, parameter_7870, parameter_7890, parameter_7880, parameter_7860)

      phi_kernel_11590, = call(self.phi_kernel_1159, phi_kernel_11530, parameter_7900)

      phi_kernel_11600, = call(self.phi_kernel_1160)

      phi_kernel_11610, phi_kernel_11611, = call(self.phi_kernel_1161, parameter_7910, phi_kernel_11600)

      phi_kernel_11620, = call(self.phi_kernel_1162, phi_kernel_11590, phi_kernel_11610)

      phi_kernel_11630, = call(self.phi_kernel_1163, phi_kernel_11620)

      phi_kernel_11640, = call(self.phi_kernel_1164)

      phi_kernel_11650, = call(self.phi_kernel_1165)

      phi_kernel_11660, = call(self.phi_kernel_1166, phi_kernel_11630, phi_kernel_11640, phi_kernel_11650)

      phi_kernel_11670, = call(self.phi_kernel_1167)

      phi_kernel_11680, = call(self.phi_kernel_1168)

      phi_kernel_11690, = call(self.phi_kernel_1169)

      phi_kernel_11700, = call(self.phi_kernel_1170)

      combine_11710, = call(self.combine_1171, phi_kernel_11660, phi_kernel_11670, phi_kernel_11680, phi_kernel_11690, phi_kernel_11700)

      phi_kernel_11720, phi_kernel_11721, = call(self.phi_kernel_1172, phi_kernel_11620, combine_11710)

      phi_kernel_11730, = call(self.phi_kernel_1173, phi_kernel_11720)

      phi_kernel_11740, = call(self.phi_kernel_1174)

      phi_kernel_11750, = call(self.phi_kernel_1175)

      phi_kernel_11760, = call(self.phi_kernel_1176)

      combine_11770, = call(self.combine_1177, phi_kernel_11660, phi_kernel_11740, phi_kernel_11750, phi_kernel_11760)

      phi_kernel_11780, phi_kernel_11781, = call(self.phi_kernel_1178, phi_kernel_11730, combine_11770)

      phi_kernel_11790, = call(self.phi_kernel_1179, phi_kernel_11780)

      phi_kernel_11800, = call(self.phi_kernel_1180, phi_kernel_11790, parameter_7920)

      phi_kernel_11810, = call(self.phi_kernel_1181)

      phi_kernel_11820, phi_kernel_11821, = call(self.phi_kernel_1182, parameter_7930, phi_kernel_11810)

      phi_kernel_11830, = call(self.phi_kernel_1183, phi_kernel_11800, phi_kernel_11820)

      phi_kernel_11840, = call(self.phi_kernel_1184, phi_kernel_11830)

      phi_kernel_11850, phi_kernel_11851, phi_kernel_11852, phi_kernel_11853, phi_kernel_11854, phi_kernel_11855, = call(self.phi_kernel_1185, phi_kernel_11840, parameter_7950, parameter_7970, parameter_7960, parameter_7940)

      phi_kernel_11860, = call(self.phi_kernel_1186, phi_kernel_11850)

      phi_kernel_11870, = call(self.phi_kernel_1187, phi_kernel_11860, parameter_7980)

      phi_kernel_11880, = call(self.phi_kernel_1188)

      phi_kernel_11890, phi_kernel_11891, = call(self.phi_kernel_1189, parameter_7990, phi_kernel_11880)

      phi_kernel_11900, = call(self.phi_kernel_1190, phi_kernel_11870, phi_kernel_11890)

      phi_kernel_11910, phi_kernel_11911, phi_kernel_11912, phi_kernel_11913, phi_kernel_11914, phi_kernel_11915, = call(self.phi_kernel_1191, phi_kernel_11900, parameter_8010, parameter_8030, parameter_8020, parameter_8000)

      phi_kernel_11920, = call(self.phi_kernel_1192, phi_kernel_11910, phi_kernel_11580)

      phi_kernel_11930, = call(self.phi_kernel_1193, phi_kernel_11920)

      phi_kernel_11940, = call(self.phi_kernel_1194, phi_kernel_11930, parameter_8040)

      phi_kernel_11950, = call(self.phi_kernel_1195)

      phi_kernel_11960, phi_kernel_11961, = call(self.phi_kernel_1196, parameter_8050, phi_kernel_11950)

      phi_kernel_11970, = call(self.phi_kernel_1197, phi_kernel_11940, phi_kernel_11960)

      phi_kernel_11980, phi_kernel_11981, phi_kernel_11982, phi_kernel_11983, phi_kernel_11984, phi_kernel_11985, = call(self.phi_kernel_1198, phi_kernel_11970, parameter_8070, parameter_8090, parameter_8080, parameter_8060)

      phi_kernel_11990, = call(self.phi_kernel_1199, phi_kernel_11930, parameter_8100)

      phi_kernel_12000, = call(self.phi_kernel_1200)

      phi_kernel_12010, phi_kernel_12011, = call(self.phi_kernel_1201, parameter_8110, phi_kernel_12000)

      phi_kernel_12020, = call(self.phi_kernel_1202, phi_kernel_11990, phi_kernel_12010)

      phi_kernel_12030, = call(self.phi_kernel_1203, phi_kernel_12020)

      phi_kernel_12040, = call(self.phi_kernel_1204)

      phi_kernel_12050, = call(self.phi_kernel_1205)

      phi_kernel_12060, = call(self.phi_kernel_1206, phi_kernel_12030, phi_kernel_12040, phi_kernel_12050)

      phi_kernel_12070, = call(self.phi_kernel_1207)

      phi_kernel_12080, = call(self.phi_kernel_1208)

      phi_kernel_12090, = call(self.phi_kernel_1209)

      phi_kernel_12100, = call(self.phi_kernel_1210)

      combine_12110, = call(self.combine_1211, phi_kernel_12060, phi_kernel_12070, phi_kernel_12080, phi_kernel_12090, phi_kernel_12100)

      phi_kernel_12120, phi_kernel_12121, = call(self.phi_kernel_1212, phi_kernel_12020, combine_12110)

      phi_kernel_12130, = call(self.phi_kernel_1213, phi_kernel_12120)

      phi_kernel_12140, = call(self.phi_kernel_1214)

      phi_kernel_12150, = call(self.phi_kernel_1215)

      phi_kernel_12160, = call(self.phi_kernel_1216)

      combine_12170, = call(self.combine_1217, phi_kernel_12060, phi_kernel_12140, phi_kernel_12150, phi_kernel_12160)

      phi_kernel_12180, phi_kernel_12181, = call(self.phi_kernel_1218, phi_kernel_12130, combine_12170)

      phi_kernel_12190, = call(self.phi_kernel_1219, phi_kernel_12180)

      phi_kernel_12200, = call(self.phi_kernel_1220, phi_kernel_12190, parameter_8120)

      phi_kernel_12210, = call(self.phi_kernel_1221)

      phi_kernel_12220, phi_kernel_12221, = call(self.phi_kernel_1222, parameter_8130, phi_kernel_12210)

      phi_kernel_12230, = call(self.phi_kernel_1223, phi_kernel_12200, phi_kernel_12220)

      phi_kernel_12240, = call(self.phi_kernel_1224, phi_kernel_12230)

      phi_kernel_12250, phi_kernel_12251, phi_kernel_12252, phi_kernel_12253, phi_kernel_12254, phi_kernel_12255, = call(self.phi_kernel_1225, phi_kernel_12240, parameter_8150, parameter_8170, parameter_8160, parameter_8140)

      phi_kernel_12260, = call(self.phi_kernel_1226, phi_kernel_12250)

      phi_kernel_12270, = call(self.phi_kernel_1227, phi_kernel_12260, parameter_8180)

      phi_kernel_12280, = call(self.phi_kernel_1228)

      phi_kernel_12290, phi_kernel_12291, = call(self.phi_kernel_1229, parameter_8190, phi_kernel_12280)

      phi_kernel_12300, = call(self.phi_kernel_1230, phi_kernel_12270, phi_kernel_12290)

      phi_kernel_12310, phi_kernel_12311, phi_kernel_12312, phi_kernel_12313, phi_kernel_12314, phi_kernel_12315, = call(self.phi_kernel_1231, phi_kernel_12300, parameter_8210, parameter_8230, parameter_8220, parameter_8200)

      phi_kernel_12320, = call(self.phi_kernel_1232, phi_kernel_12310, phi_kernel_11980)

      phi_kernel_12330, = call(self.phi_kernel_1233, phi_kernel_12320)

      phi_kernel_12340, = call(self.phi_kernel_1234)

      phi_kernel_12350, = call(self.phi_kernel_1235, phi_kernel_12330, phi_kernel_12340)

      phi_kernel_12360, = call(self.phi_kernel_1236)

      phi_kernel_12370, = call(self.phi_kernel_1237)

      phi_kernel_12380, = call(self.phi_kernel_1238)

      phi_kernel_12390, = call(self.phi_kernel_1239)

      combine_12400, = call(self.combine_1240, phi_kernel_8310, phi_kernel_12360, phi_kernel_12370, phi_kernel_12380, phi_kernel_12390)

      phi_kernel_12410, phi_kernel_12411, = call(self.phi_kernel_1241, phi_kernel_12350, combine_12400)

      phi_kernel_12420, = call(self.phi_kernel_1242, phi_kernel_12410)

      phi_kernel_12430, = call(self.phi_kernel_1243, phi_kernel_12420, parameter_8240)

      phi_kernel_12440, = call(self.phi_kernel_1244)

      phi_kernel_12450, phi_kernel_12451, = call(self.phi_kernel_1245, parameter_8250, phi_kernel_12440)

      phi_kernel_12460, = call(self.phi_kernel_1246, phi_kernel_12430, phi_kernel_12450)

      phi_kernel_12470, = call(self.phi_kernel_1247, phi_kernel_12460)

      phi_kernel_12480, = call(self.phi_kernel_1248)

      phi_kernel_12490, = call(self.phi_kernel_1249)

      phi_kernel_12500, = call(self.phi_kernel_1250, phi_kernel_12470, phi_kernel_12480, phi_kernel_12490)

      phi_kernel_12510, = call(self.phi_kernel_1251)

      combine_12520, = call(self.combine_1252, phi_kernel_12500, phi_kernel_12510)

      phi_kernel_12530, phi_kernel_12531, = call(self.phi_kernel_1253, phi_kernel_12460, combine_12520)

      call(self.shadow_output_1254, phi_kernel_12530)

    return ret_lambda_module_629_block00

    

  def __call__(self, call, *args, **kwargs):

    self.SetArgs(args)

    self.SetKeywordArgs(kwargs)

    return call(self.module_629, blocks=[[(self.module_629_block00,)]])


