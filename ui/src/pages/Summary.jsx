import { Button } from '@mui/material'
import React, { useState } from 'react'
import { summaryCompletion } from "../api/chat.api";
import { toast } from "react-toastify";
import Upload from '../components/Upload';

export default function Summary() {
    const [summry, setSummary] = useState("");
    const createSummary = async () => {
        const { response, err } = await summaryCompletion({ prompt: "" });
        if (response) {
            setSummary(response.data);
        }
        if (err) {
            toast.error(err.message);
        }
    }

    return (
        <div>
            <Upload />
            <Button onClick={createSummary}>Create Summary</Button>
            <div>{summry}</div>
        </div>

    )
}
