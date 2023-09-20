import React, { useState, useEffect, useImperativeHandle, useRef, forwardRef } from 'react'
import { Button, Input, Select, Popconfirm } from "antd"
const options1 = [{
    value: 'func1',
    label: 'func1',
},
{
    value: 'func2',
    label: 'func2',
}]
const MyTable = (props, ref) => {
    useImperativeHandle(ref, () => ({
        data
    }));
    const { sourceData, type } = props;
    const [options, setOptions] = useState([]);
    const [data, setData] = useState([]);
    const [count, setCount] = useState(1);
    useEffect(() => {
        type !== "show" && setOptions(options1)
        setData(sourceData)
    }, []);
    const handleChange = (e, index, type) => {
        data[index][type] = type === "handle" ? e : e.target.value;
        setData([...data]);

    }
    const handleDelete = (item, index) => {
        setData(data.filter((item, i) => i != index))
    }
    const add = () => {
        let t = count + 1;
        setCount(t);
        setData([...data, { source: "", dest: "", handle: "", key: t }])
    }
    return (
        <>{type !== "show" && <Button type='primary' style={{ marginBottom: "6px" }} onClick={add}>Add New Mapping</Button>}
            <ul className='my-table'>
                <li className='title'>
                    <div className='source'>Source</div>
                    <div className='dest'>Destination</div>
                    <div className='handle'>Handle Function</div>
                    {type !== "show" && <div className='action'>Action</div>}
                </li>
                {data.map((item, index) => <li className='item' key={index}>
                    <div className='source'>{type === "show" ? item.source : <Input value={item.source} onChange={(e) => handleChange(e, index, "source")} />}</div>
                    <div className='dest'>{type === "show" ? item.dest : <Input value={item.dest} onChange={(e) => handleChange(e, index, "dest")} />}</div>
                    <div className='handle'>{type === "show" ? item.handle : <Select value={item.handle}
                        style={{ width: 120, }}
                        onChange={(v) => handleChange(v, index, "handle")}
                        options={options} />}</div>
                    {type !== "show" && <div className='action'>
                        <Popconfirm title="Sure to delete?" onConfirm={() => handleDelete(item, index)}>
                            <a>Delete</a>
                        </Popconfirm>
                    </div>}
                </li>)
                }

            </ul >
        </>
    )
}
export default forwardRef(MyTable);
