import ChartDrag from "../dragcomp/ChartDrag";
import FetchData from "../dragcomp/FetchDataDrag";
import PublishDrag from "../dragcomp/PublishDrag";
import ReportDrag from "../dragcomp/ReportDrag";

export const typeMap = {
    1: { comp: <FetchData />, title: "Fetch Data Config" }, //fetch data
    2: { comp: <ChartDrag />, title: "Generate Chart Config" }, //generate chart
    2: { comp: <ReportDrag />, title: "Generate Report Config" }, //generate report
    3: { comp: <PublishDrag />, title: "Publish Config" }  //publish
}