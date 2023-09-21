import React, { memo, useState } from 'react';
import { CloseOutlined } from '@ant-design/icons';

import { Handle } from 'react-flow-renderer';
import { Drawer } from "antd"
import { typeMap } from './config';

export default memo(({ data, id, isConnectable }: any) => {
  const [open, setOpen] = useState(true);

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
        <div className="nodelabel" onClick={() => setOpen(true)}>{data.label}</div>
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
      <Drawer title={typeMap[3].title} placement="right" onClose={() => setOpen(false)} open={open}>
        {typeMap[3].comp}
      </Drawer>
    </>
  );
});
