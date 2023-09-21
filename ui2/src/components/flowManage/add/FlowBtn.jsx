import React, { useRef, useState } from 'react'
import { Space, Input, Button } from "antd"
import { handleData } from '../../../api/common.api';
const { TextArea } = Input;

export default function FlowBtn(props) {
    const [flow, setFlow] = useState();
    const flowRef = useRef()
    const getFlow = async () => {
        console.log("getFlow", props)
        const { response } = await handleData({ action: "getFlow", data: "" });
        // if (response) {
        //     setFlow(response.data);
        // }
    }
    const testFlow = async () => {
        const { response } = await handleData({ action: "testFlow", data: "" });
    }
    return (
        <div className='filter'>
            <Space>
                <TextArea rows={4}
                    placeholder="Please describe your work flow"
                    autoSize={{
                        minRows: 2,
                        maxRows: 6,
                    }}
                    style={{ width: '400px' }}
                />
                <Button type="primary" onClick={getFlow}>Create workflow</Button>
                <Button type="primary" onClick={testFlow}>Test Workflow</Button>
            </Space>
        </div>
    )
}
