// return react button component
import React from "react";
import { FormControl } from "@mui/material";
import { InputLabel } from "@mui/material";
import { Input } from "@mui/material";
import { FormHelperText, FormControlLabel } from "@mui/material";
import { Button } from "@mui/material";
import { RadioGroup, Radio } from "@mui/material";
import { set, useForm } from "react-hook-form";
import axios from "axios";

const URL = "http://localhost:3000";

// export default function Button() {
function HebrewTextForm(props) {
  const { register, handleSubmit } = useForm();

  const onSubmit = async (data) => {
    props.setIsLoading(true);
    // alert(JSON.stringify(data));
    const response = axios.get(`${URL}/text`, { params: data }).then((res) => {
      props.setOutputText(res.data);
      new Promise((resolve) => setTimeout(resolve, 1000)).then(() => props.setIsLoading(false));
      // props.setIsLoading(false);
    });
    // props.setOutputText(response.data);
  };

  return (
    <FormControl>
      <InputLabel htmlFor="my-input"></InputLabel>
      <Input
        id="my-input"
        {...register("text")}
        defaultValue="יש 5 מכוניות"
        aria-describedby="my-helper-text"
        rows={8}
        minRows={4}
      />
      <FormHelperText id="my-helper-text">הוסף טקסט שתרצה להמיר על פי הטיה מגדרית</FormHelperText>

      <RadioGroup
        aria-labelledby="demo-radio-buttons-group-label"
        defaultValue="classic"
        row={true}
        {...register("kind")}
        name="radio-buttons-group"
      >
        <FormControlLabel value="classic" control={<Radio />} label="קלאסי" {...register("kind")} />
        <FormControlLabel value="random-forest" control={<Radio />} label="יער אקראי" {...register("kind")} />
        <FormControlLabel value="other" control={<Radio />} label="אחר" {...register("kind")} />
      </RadioGroup>

      <Button onClick={handleSubmit(onSubmit)} variant="contained">
        שלח
      </Button>
    </FormControl>
  );
}

export default HebrewTextForm;
