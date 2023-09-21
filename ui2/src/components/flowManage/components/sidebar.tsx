import React from 'react';

export default () => {
  const onDragStart = (event: any, nodeType: any, nodeLabel: any) => {
    event.dataTransfer.setData('application/reactflow', nodeType);
    event.dataTransfer.setData('application/label', nodeLabel);
    event.dataTransfer.effectAllowed = 'move';
  };
  const onDragEnd = () => {

  }
  return (
    <aside>
      <div className="description">Drag to add flow:</div>
      {/* <div
        className="dndnode input"
        onDragStart={(event) => {
          event.stopPropagation();
          onDragStart(event, 'input');
        }}
        draggable
      >
        开始节点
      </div> */}
      <div
        className="dndnode"
        onDragStart={(event) => {
          event.stopPropagation();
          onDragStart(event, 'custom', 'Fetch Data');
        }}
        onDragEnd={(event) => {
          event.stopPropagation();
          onDragEnd(event, 'custom', 'Fetch Data');
        }}
        draggable
      >
        Fetch Data
      </div>
      <div
        className="dndnode"
        onDragStart={(event) => {
          event.stopPropagation();
          onDragStart(event, 'custom', 'generate  report');
        }}
        draggable
      >
        generate report
      </div>
      <div
        className="dndnode"
        onDragStart={(event) => {
          event.stopPropagation();
          onDragStart(event, 'custom', 'generate chart');
        }}
        draggable
      >
        generate chart
      </div>
      <div
        className="dndnode"
        onDragStart={(event) => {
          event.stopPropagation();
          onDragStart(event, 'custom', 'Publish');
        }}
        draggable
      >
        Publish
      </div>
      {/* <div
        className="dndnode output"
        onDragStart={(event) => {
          event.stopPropagation();
          onDragStart(event, 'output');
        }}
        draggable
      >
        结束节点
      </div> */}
    </aside>
  );
};
