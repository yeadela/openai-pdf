import FetchData from "../dragcomp/FetchDataDrag";
import PublishDrag from "../dragcomp/PublishDrag";

export const typeMap = {
    1: { comp: <FetchData />, title: "Fetch Data Config" }, //fetch data
    2: { comp: <FetchData />, title: "Generate Report Config" }, //generate port
    3: { comp: <PublishDrag />, title: "Publish Config" }  //publish
}