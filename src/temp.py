class ControlBooleans:
  	def __init__(self):
        self.MtoEtoRA=False # booleans to indicate data forwarding in the end of the same cycle, then set it to false
        self.MtoEtoRB=False
        self.EtoDtoR1=False
        self.EtoDtoR2=False
        self.EtoEtoRA=False
        self.EtoEtoRB=False
        self.MtoM=False # this is always to MDR(rs2)
        self.decode_stall=False
        self.fetch_stall=False
    
forward_bool = ControlBooleans()


def fetch(stage):
    # to do here
    # if terminate==1, return
    # operation queue will be used in the buffer update stage, not here.
    # fetch the instruction using the value in PC
    # compare it to BTB to check if that is a branch/jump. If it is, update PC to the target.
    # remember to enqueue the PC into the decode_PC_queue

def decode(stage):
    # if terminate==1, return
    # check the operation queue. If empty, then operate. Else, don't operate and pop.
    mtod=True
    if(!control_module.decode_deque_signal())
    {
    	# decode stage is inactive. Perform other tasks
      	if control_module.MtoEcode==-2:
      		return
      	forward_bool.decode_stall=True
      	forward_bool.fetch_stall=True
      	if control_module.MtoEcode==-1:
      		mtod=True
      	#	return # M to D stall
      	if control_module.MtoEcode==21:
      		forward_bool.MtoEtoRA=True
      		return
      	if control_module.MtoEcode==22:
      		forward_bool.MtoEtoRB=True
      		return
      	if control_module.MtoEcode==23:
      		forward_bool.MtoEtoRA=True
      		forward_bool.MtoEtoRB=True
      		return
    }
    # decode the instruction first in the IR
    control_module.decode(registers.ReadIR(),IAGmodule.PC)
    # check for hazards using the hazard table.
    hazard_code=hazard_module.check_dependance() # tentative !!
    # if hazard, perform corrective measures here and return. Do not execute further code
    to_return=False
    if hazard_code[0]!=-1 or hazard_code[0]!=-1: # data hazard!
      # code here for data hazard
      # first handling hazard[0] then hazard[1]
      if hazard_code[1]!=-1:
      	if hazard_code[1]==0:
           	control_module.mem_ForwardingQueue.append(0) # set boolean to true in memory module
        elif hazard_code[1]==11:
        	forward_bool.MtoEtoRA=True
        elif hazard_code[1]==12:
  			forward_bool.MtoEtoRB=True
        elif hazard_code[1]==13:
          	forward_bool.MtoEtoRA=True
            forward_bool.MtoEtoRB=True
        elif hazard_code[1]==21:
        	control_module.ForwardingQueue.append(hazard_code[1])
            #push null instruction in hazard table
            #forward_bool.stall=True
            self.decode_operation.append(21)
            #forward_bool.decode_stall=True
            control_module.fetch_set_NOP() # tentative!!
            #control_module.decode_set_NOP() # edit
            # push 1 nop and the decoded instruction in the queues
            control_module.execute_set_NOP()
            control_module.memory_set_NOP()
            control_module.register_set_NOP()
            control_module.execute_set_operate()
            control_module.memory_set_operate()
            control_module.register_set_operate()
        elif hazard_code[1]==22:
          	control_module.ForwardingQueue.append(hazard_code[1])
            #push null instruction in hazard table
            self.decode_operation.append(22)
            #forward_bool.decode_stall=True
            control_module.fetch_set_NOP() # tentative!!
            #control_module.decode_set_NOP() # edit
            # push 1 nop and the decoded instruction in the queues
            control_module.execute_set_NOP()
            control_module.memory_set_NOP()
            control_module.register_set_NOP()
            control_module.execute_set_operate()
            control_module.memory_set_operate()
            control_module.register_set_operate()
        elif hazard_code[1]==23:
          	control_module.ForwardingQueue.append(hazard_code[1])
            #push null instruction in hazard table
            #forward_bool.decode_stall=True # in th
            control_module.fetch_set_NOP() # tentative!!
            self.decode_operation.append(23)
            #control_module.decode_set_NOP() # edit
            # push 1 nop and the decoded instruction in the queues
            control_module.execute_set_NOP()
            control_module.memory_set_NOP()
            control_module.register_set_NOP()
            control_module.execute_set_operate()
            control_module.memory_set_operate()
            control_module.register_set_operate()
        elif hazard_code[1]==31:
        	forward_bool.EtoEtoRA=True
        elif hazard_code[1]==32:
          	forward_bool.EtoEtoRB=True
        elif hazard_code[1]==33:
          	forward_bool.EtoEtoRA=True
            forward_bool.EtoEtoRB=True
        elif hazard_code[1]==41:
          	# stall code MtoD, handle similar to that done in stalling case
            self.decode_operation.append(-1)
            forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
        elif hazard_code[1]==42:
          	# stall code MtoD, handle similar to that done in stalling case
            self.decode_operation.append(-1)
            forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
        elif hazard_code[1]==43:
          	# stall code MtoD, handle similar to that done in stalling case
            self.decode_operation.append(-1)
            forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
        elif hazard_code[1]==51:
          	# stall code MtoD, handle similar to that done in stalling case
            forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
        elif hazard_code[1]==52:
          	# stall code MtoD, handle similar to that done in stalling case
            forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
        elif hazard_code[1]==53:
        	# stall code MtoD, handle similar to that done in stalling case
            forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
        elif hazard_code[1]==61:
          	forward_bool.EtoDtoR1=True
          	forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
            to_return=True
        elif hazard_code[1]==62:
          	forward_bool.EtoDtoR2=True
          	forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
            to_return=True
        elif hazard_code[1]==63:
          	forward_bool.EtoDtoR1=True
            forward_bool.EtoDtoR2=True
          	forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
            to_return=True
        elif hazard_code[1]==71:
          	buffers.R1bool=True
            buffers.RAtemp=buffers.RZ
        elif hazard_code[1]==72:
          	buffers.R2bool=True
            buffers.RBtemp=buffers.RZ
        elif hazard_code[1]==73:
          	buffers.R1bool=True
            buffers.RAtemp=buffers.RZ
        	buffers.R2bool=True
            buffers.RBtemp=buffers.RZ
            
      if hazard_code[0]!=-1:
      	if hazard_code[0]==0:
           	control_module.mem_ForwardingQueue.append(0) # set boolean to true in memory module
        elif hazard_code[0]==11:
        	forward_bool.MtoEtoRA=True
        elif hazard_code[0]==12:
  			forward_bool.MtoEtoRB=True
        elif hazard_code[0]==13:
          	forward_bool.MtoEtoRA=True
            forward_bool.MtoEtoRB=True
        elif hazard_code[0]==21:
        	control_module.ForwardingQueue.append(hazard_code[0])
            #push null instruction in hazard table
            #forward_bool.stall=True
            self.decode_operation.append(21)
            #forward_bool.decode_stall=True
            control_module.fetch_set_NOP() # tentative!!
            #control_module.decode_set_NOP() # edit
            # push 1 nop and the decoded instruction in the queues
            control_module.execute_set_NOP()
            control_module.memory_set_NOP()
            control_module.register_set_NOP()
            control_module.execute_set_operate()
            control_module.memory_set_operate()
            control_module.register_set_operate()
        elif hazard_code[0]==22:
          	control_module.ForwardingQueue.append(hazard_code[0])
            #push null instruction in hazard table
            self.decode_operation.append(22)
            #forward_bool.decode_stall=True
            control_module.fetch_set_NOP() # tentative!!
            #control_module.decode_set_NOP() # edit
            # push 1 nop and the decoded instruction in the queues
            control_module.execute_set_NOP()
            control_module.memory_set_NOP()
            control_module.register_set_NOP()
            control_module.execute_set_operate()
            control_module.memory_set_operate()
            control_module.register_set_operate()
        elif hazard_code[0]==23:
          	control_module.ForwardingQueue.append(hazard_code[0])
            #push null instruction in hazard table
            #forward_bool.decode_stall=True # in th
            control_module.fetch_set_NOP() # tentative!!
            self.decode_operation.append(23)
            #control_module.decode_set_NOP() # edit
            # push 1 nop and the decoded instruction in the queues
            control_module.execute_set_NOP()
            control_module.memory_set_NOP()
            control_module.register_set_NOP()
            control_module.execute_set_operate()
            control_module.memory_set_operate()
            control_module.register_set_operate()
        elif hazard_code[0]==31:
        	forward_bool.EtoEtoRA=True
        elif hazard_code[0]==32:
          	forward_bool.EtoEtoRB=True
        elif hazard_code[0]==33:
          	forward_bool.EtoEtoRA=True
            forward_bool.EtoEtoRB=True
        elif hazard_code[0]==41:
          	# stall code MtoD, handle similar to that done in stalling case
            self.decode_operation.append(-1)
            forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
        elif hazard_code[0]==42:
          	# stall code MtoD, handle similar to that done in stalling case
            self.decode_operation.append(-1)
            forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
        elif hazard_code[0]==43:
          	# stall code MtoD, handle similar to that done in stalling case
            self.decode_operation.append(-1)
            forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
        elif hazard_code[0]==51:
          	# stall code MtoD, handle similar to that done in stalling case
            forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
        elif hazard_code[0]==52:
          	# stall code MtoD, handle similar to that done in stalling case
            forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
        elif hazard_code[0]==53:
        	# stall code MtoD, handle similar to that done in stalling case
            forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
        elif hazard_code[0]==61:
          	forward_bool.EtoDtoR1=True
          	forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
            to_return=True
        elif hazard_code[0]==62:
          	forward_bool.EtoDtoR2=True
          	forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
            to_return=True
        elif hazard_code[0]==63:
          	forward_bool.EtoDtoR1=True
            forward_bool.EtoDtoR2=True
          	forward_bool.decode_stall=True
      		forward_bool.fetch_stall=True
            to_return=True
        elif hazard_code[0]==71:
          	buffers.R1bool=True
            buffers.RAtemp=buffers.RZ
        elif hazard_code[0]==72:
          	buffers.R2bool=True
            buffers.RBtemp=buffers.RZ
        elif hazard_code[0]==73:
          	buffers.R1bool=True
            buffers.RAtemp=buffers.RZ
        	buffers.R2bool=True
            buffers.RBtemp=buffers.RZ
        if mtod or to_return:
      		return
    # check for branch misprediction here, use Decode_input_branch_prediction
    # read the registers or PC or forwarded value here and update RA and RB with those values. Use control signals for MuxA and MuxB to set them!!!!
    # code for executing ALU for branch misprediction here.
    if !control_module.jump:
    	control_module.ALUexecute(control_module.ALUOp, control_module.ALUcontrol, RA, RB)
    # use branch prediction from the buffer
    if branch_misprediction: 
      # code here for handling branch misprediction
      control_module.execute_set_operate()
      control_module.memory_set_operate()
	  control_module.register_set_operate()
      return 
    # push NOPs whenever needed, call the exexute_set_NOP etc methods is ControlModule according to hazard code
    # if misprediction, perform corrective measures here and return if necessary follow steps given in documentation to resolve the hazard by stalling/data forwarding.
    # in case of jalr, compute effective address and update decode_output_PC_temp by that value.
    # if all good, push the decoded the signals into the queues.
    
    control_module.execute_set_operate()
    control_module.memory_set_operate()
	control_module.register_set_operate()
#MUXA, MUXB functionality needs to be implemented w/o the muxes!!!
def execute(stage): # ALU
    # dequeue from the control signals. Check if we need to operate or not
    #False == NOP, 
    if(!control_module.execute_deque_signal()){ # this function returns False if memory is in NOP. Also, all control_module.ALUop, etc are updated to 0 in case of NOP, or correct value if OP
    	# perform other tasks and return
    }
	# can use control_module.ALUop etc directly to use as arguments to ALU.
    ALUmodule.ALUexecute(control_module.ALUOp, control_module.ALUcontrol,buffer.getRA, buffer.getRB)
    buffer.setRZtemp(ALUmodule.output32)	#simple execution
    #add this code at the end of cycle
    #if(EtoE){
      #buffer.set
    #}  
    
    
def mem_access(stage):
    # dequeue from the control signals. Check if we need to operate or not
    if(!control_module.memory_deque_signal()) # this function returns False if memory is in NOP. Also, all control_module.MemRead, etc are updated to 0 in case of NOP, or correct value if OP
    {
      # perform other tasks and return
    }
    # acess memory and update temp memory buffers (RM_temp)
    memory.AccessMemory(control_module.MemRead, control_module.MemWrite, buffer.getRZ(), control_module.BytesToAccess, buffer.getRM()) # why RMtemp? RM is updated at the end of cycle
    # check forwarding
    if len(control_module.mem_ForwardQueue) != 0:
    {
      # check forwarding code
      # if MtoE
      # make MtoEToRA or MtoEtoRB true on the basis of encoding received
      # if MtoM
      MtoM = True
    }
    # set RYtemp according to values and MuxY control 
    if control_module.MuxYSelect == 0:
      buffer.RYtemp = buffer.getRZ()
    elif control_module.MuxYSelect == 1:
      buffer.RYtemp = memory.MDR
	elif control_module.MuxYSelect == 2:
      buffer.RYtemp = buffers.Fetch_output_PC_temp+4 # contains PC+4 #PC Buffer use karun ? ya IAG module ka PC 
    # 

def reg_writeback(stage):
    # dequeue from the control signals. Check if we need to operate or not
    if(!control_module.register_deque_signal()){ # this function returns False if reg_write_back is in NOP. Also, all control_module.ALUop, etc are updated to 0 in case of NOP, or correct value if OP
    	# perform other tasks and return
    }
    registers.WriteGpRegisters(control_module.rd, control_module.RegWrite, buffer.getRY())

def buffer_update():
  #first update the output buffers, 
  #then forward   
  #temp to Buffer data transfer
	if !forward_bool.fetch_stall:
		buffer.setR1(buffer.getR1temp)
        buffer.setR2(buffer.getR2temp)
		#fetch ke konse buffer hain?
    if !forward_bool.decode_stall:
		buffer.setRA(buffer.getRAtemp)
        buffer.setRB(buffer.getRBtemp)
		#decode ke konse buffer hain aur?
	buffer.setRZ(buffer.getRZtemp)	#RZ update
    buffer.setRM(buffer.getRMtemp)
    #RY temp toh nahi hai na kuchh?
	
  	#forward data in priority
	if forward_bool.MtoM:
		buffer.setRM(buffer.MDR, True) # RM is updated to MDR of memory in case of M to M forwarding
		forward_bool.MtoM = False
    
    if forward_bool.MtoEtoRA:	#MDR to RA
		buffer.setRA(buffer.MDR, True) 
		forward_bool.MtoEtoRA = False
      
    if forward_bool.MtoEtoRB:	#MDR to RB
		buffer.setRB(buffer.MDR, True) 
		forward_bool.MtoEtoRB = False
      
    if forward_bool.EtoEtoRA:	#RZ to RA(rs1)
		buffer.setRA(buffer.getRZ, True)
		forward_bool.EtoEtoRA = False
      
    if forward_bool.EtoEtoRB:	#RZ to RB(rs2)
		buffer.setRB(buffer.getRZ, True)
		forward_bool.EtoEtoRB = False
    
    if forward_bool.EtoDtoR1:
  		buffer.setR1(buffer.getRZ, True)
		forward_bool.EtoEtoR1 = False
        
	if forward_bool.EtoDtoR2:
		buffer.setR2(buffer.getRZ, True)
		forward_bool.EtoEtoR2 = False
        
        #resetting stall signals
	if !forward_bool.fetch_stall:
		forward_bool.fetch_stall = True

    if !forward_bool.decode_stall:
		forward_bool.decode_stall = True

    
      
def RunSim():
    clock=1
    while(True):
        # run the stages here, preferably in reverse order.
        # update the buffers in the end