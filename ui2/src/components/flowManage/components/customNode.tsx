import React, { memo } from 'react';
import { CloseOutlined } from '@ant-design/icons';

import { Handle } from 'react-flow-renderer';

export default memo(({ data, id, isConnectable }: any) => {


  return (
    <>
      <Handle
        type="target"
        position="top"
        className="my_handle"
        onConnect={(params) => console.log('handle onConnect', params)}
        isConnectable={isConnectable}
      />

      <div className="nodeContent" style={data.style}>
        <div className="nodelabel" style={{ color: "red" }}>{data.label}</div>
        <div className="close">
          <CloseOutlined
            onClick={(e) => {
              e.stopPropagation();
              data.onChange(id);
            }}
            className="icon-close"
          />
        </div>
      </div >

      <Handle
        type="source"
        position="bottom"
        id="a"
        className="my_handle"
        isConnectable={isConnectable}
      />
    </>
  );
});
