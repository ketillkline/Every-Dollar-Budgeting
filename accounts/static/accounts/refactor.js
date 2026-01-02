class BillManager {
    constructor() {
        this.validStates = ["IDLE", "ADDING", "EDITING"];
        this.state = {
            mode: "IDLE"
        };

    }

    changeState(state){
        if (!this.validStates.includes(state)){
            throw new Error(`Invalid state: ${state}.`);
        }
        this.state.mode = state;
    }

    updateUI(){
        functionMap = {
            "IDLE": this.idleUI(),
            "ADDING": this.addingUI(),
            "EDITING": this.editingUI()
        }
    }

    setupEvents(){

    }

    addBill(){
        this.changeState("ADDING");

        this.changeState("IDLE");
    }

    editBill() {
        this.changeState("EDITING");

        this.changeState("IDLE");
    }

}